from umath import sqrt, fabs, copysign
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from hub import beepLow, hub, wait

_PROFILE = None # values from 5 (smallest values for the motors used) up to at least 100 (https://docs.pybricks.com/en/stable/pupdevices/motor.html)
_AXLE_TRACK = 140
_DEFAULT_DRIVE_SPEED = 400

def tuple_or_value(first, second)->tuple:
    return (first, second) if first != second else first

class Drive:
    def __init__(self):
        # https://github.com/pybricks/support/issues/1840
        hub.imu.settings(angular_velocity_threshold=1, acceleration_threshold=1000)

        # hub.imu.settings(heading_correction=361) # only available in latest build

        self.left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE, profile=_PROFILE)
        self.right_motor =Motor(Port.B, Direction.CLOCKWISE, profile=_PROFILE)

        self.drive_base = DriveBase(self.left_motor, self.right_motor, wheel_diameter=56, axle_track=_AXLE_TRACK)

        self.drive_base.use_gyro(True)
        self.drive_base.settings(turn_rate=40)
        self.drive_base.settings(straight_speed=_DEFAULT_DRIVE_SPEED)

        self.acceleration_decelerations=[]

    def get_acceleration_deceleration(self):
        """Get currenct acceleration/deceleration value(s)

        Returns:
            number or tupple: the acceleration/deceleration value(s) in mm/s^2
        """
        return self.drive_base.settings()[1]
    
    
    def set_acceleration_deceleration(self, acceleration:float=None, deceleration:float=None):
        """Set acceleration and/or deceleration speed

        Args:
            acceleration (float, optional): Set the straight acceleration speed in mm/s^2. Values for middle motor: 24-9775 mm/s^2. Defaults to None.
            deceleration (float, optional): Set the straight deceleration speed in mm/s^2. Values for middle motor: 24-9775 mm/s^2. Defaults to None.
        """
        straight_acceleration_deceleration = self.drive_base.settings()[1]
        
        # make tuple
        if not isinstance(straight_acceleration_deceleration, tuple):
            straight_acceleration_deceleration = (straight_acceleration_deceleration,straight_acceleration_deceleration)
        straight_acceleration_deceleration = (acceleration if acceleration is not None else straight_acceleration_deceleration[0],
             deceleration if deceleration is not None else straight_acceleration_deceleration[1])
        self.drive_base.settings(straight_acceleration=straight_acceleration_deceleration)

    def push_and_set_acceleration_deceleration(self, acceleration:float=None, deceleration:float=None)->None:
        self.acceleration_decelerations.append(self.get_acceleration_deceleration())
        self.set_acceleration_deceleration(acceleration, deceleration)

    def pop_and_set_acceleration_deceleration(self)->tuple:
        assert len(self.acceleration_decelerations)>0
        acceleration_deceleration = self.acceleration_decelerations.pop()
        self.drive_base.settings(straight_acceleration=acceleration_deceleration)
        return acceleration_deceleration

    def get_straight_speed(self)->float:
        """Get straight speed

        Returns:
            float: straight speed in mm/s
        """
        return self.drive_base.settings()[0]
    
    def set_straight_speed(self, speed:float)->None:
        """Set straight speed

        Args:
            speed (float): Straight speed in mm/s
        """
        self.drive_base.settings(straight_speed=speed)

    def get_straight_deceleration(self)->float:
        """Get straight deceleration

        Returns:
            float: straight deceleration in mm/s^2
        """
        # https://docs.pybricks.com/en/stable/robotics.html#
        deceleration = drive.drive_base.settings()[1]
        if isinstance(deceleration, tuple):
            deceleration = deceleration[1]
        return deceleration

    # Source for the PID controller: https://fll-pigeons.github.io/gamechangers/gyro_pid.html (PID program using DriveBase)
    # Added deceleration.
    def drive_to(self, distance:float, target_angle:float=0.0, speed:float=None, then: Stop = Stop.HOLD, straight_acceleration:float=None, abort_when_stalled: bool= True):
        """Drive distance forward/backward to given target angle.
        The target angle should not deviate to much from the current angle. If so consider a turn first. 

        Args:
            distance (float): Distance in mm. Positive values to drive foward, negative value to drive backward.
            target_angle (float, optional): Target angle. Defaults to 0.0.
            speed (float, optional): Straight speed. Defaults to default straight speed.
            then (Stop, optional): What to do after coming to a standstill. Defaults to Stop.HOLD.
            straight_acceleration (float, optional): Set the straight acceleration speed in mm/s^2. Values for middle motor: 24-9775 mm/s^2. Defaults to None.
        """
        loop_time = 5  # time per loop in milliseconds        
        target_distance = distance # target distance
        target_speed = speed if speed is not None else self.get_straight_speed() # target speed of robot in mm/s
        k_p = 5 #  3 # the Constant 'K' for the 'p' proportional controller

        integral = 0 # initialize
        k_i = 0.06 # 0.025 #  the Constant 'K' for the 'i' integral term

        derivative = 0 # initialize
        lastError = 0 # initialize
        k_d = 37.5 # 3 #  the Constant 'K' for the 'd' derivative term

        start_distance = self.drive_base.distance()
        delta_from_start = self.drive_base.distance()-start_distance    # if the robot drives backward, self.drive_base.distance() yields negative values
        delta_distance = fabs(target_distance)-fabs(delta_from_start)

        self.push_and_set_acceleration_deceleration(straight_acceleration)

        while (delta_distance>0):
            error = self.drive_base.angle()-target_angle # proportional 
            if (error == 0):
                integral = 0
            else:
                integral = integral + error    
            derivative = error - lastError  
            
            correction = (k_p*(error) + k_i*(integral) + k_d*derivative) * -1
            
            # linear deceleration to target distance
            # Usual equations for accelerated/decelerated movement 
            #   v = a*t
            #   s = 1/2*a*t^2
            # lead to
            #   v = sqrt(2*s*a)
            
            deceleration_speed=sqrt(2*delta_distance*self.get_straight_deceleration())
            speed = min(target_speed,deceleration_speed)
            speed = copysign(speed,distance)

            self.drive_base.drive(speed, correction)

            lastError = error  
            
            # print("distance: " + str(self.drive_base.distance()) + "; error " + str(error) + "; integral " + str(integral) + "; correction " + str(correction)  )    
            wait(loop_time)

            delta_from_start = self.drive_base.distance()-start_distance
            delta_distance = fabs(target_distance)-fabs(delta_from_start)
            # print("Target distance: ", target_distance, "; Start distance: ", start_distance, "; Delta distance from start: ", delta_from_start, "; Delta distance to target", delta_distance)
        
            if abort_when_stalled and self.drive_base.stalled():
                beepLow()
                break

        # to implement the "then"
        self.drive_base.straight(0,then)
        self.pop_and_set_acceleration_deceleration()

    def arc(self, radius:float, angle:float=None, distance:float=None, then=Stop.HOLD, wait=True, straight_acceleration:float=None, straight_deceleration:float=None):
        """Drives an arc (a partial circle) with a given radius. You can specify how far to drive using either an angle or a distance.
        With a positive radius, the robot drives along a circle to its right. With a negative radius, the robot drives along a circle to its left.
        You can specify how far to travel along that circle as an angle (degrees) or distance (mm). A positive value means driving forward along the circle. Negative means driving in reverse.

        Args:
            radius (float): Radius of the circle in mm
            angle (float, optional): Angle to drive along the circle. Defaults to None.
            distance (float, optional): Distance to drive along the circle, measured at the center of the robot. Defaults to None.
            then (Stop, optional): What to do after coming to a standstill. Defaults to Stop.HOLD.
            wait (bool, optional): Wait for the maneuver to complete before continuing with the rest of the program.. Defaults to True.
            straight_acceleration (float, optional): The straight acceleration speed in mm/s^2. Values for middle motor: 24-9775 mm/s^2. Defaults to None.
        """
        self.push_and_set_acceleration_deceleration(straight_acceleration, straight_deceleration)
        self.drive_base.arc(radius, angle=angle, distance=distance, then=then, wait=wait)
        self.pop_and_set_acceleration_deceleration()

    def distance(self)->float:
        """Get the distance in mm (since last reset)

        Returns:
            float, mm: Distance in mm (since last reset)
        """
        return self.drive_base.distance()

    def angle(self)->float:
        """Get the angle of the drive base.

        Returns:
            float, deg: accumulated angle since last reset.
        """
        return self.drive_base.angle()

    def wait_for_ready():
        pass # while not hub.imu.ready():
            # wait(200)

    def straight(self, distance:float, then: Stop = Stop.HOLD, wait: bool=True, straight_acceleration:float=None, straight_deceleration:float=None):
        """Drives straight for a given distancen then stop.

        Args:
            distance (float, mm): Distance to drive.
            then (Stop, optional): What to do after coming to a standstill. Defaults to Stop.HOLD.
            wait (bool, optional): Wait for the maneuver to complete before continuing with the rest of the program. Defaults to True.
            straight_acceleration (float, optional): The straight acceleration speed in mm/s^2. Values for middle motor: 24-9775 mm/s^2. Defaults to None.
            straight_deceleration (float, optional): The straight deceleration speed in mm/s^2. Values for middle motor: 24-9775 mm/s^2. Defaults to None.
        """
        self.push_and_set_acceleration_deceleration(straight_acceleration, straight_deceleration)
        self.drive_base.straight(distance, then=then, wait=wait)
        self.pop_and_set_acceleration_deceleration()

    def turn_and_drive(self, angle:float, distance: float, then: Stop = Stop.HOLD, wait: bool=True, straight_acceleration:float=None, straight_deceleration:float=None):
        """Turn to the given angle before driving straight for the given distance.

        Args:
            angle (float): The angle to turn to before driving
            distance (float, mm): The distance to drive.
            then (Stop, optional): What to do after coming to a standstill. Defaults to Stop.HOLD.
            wait (bool, optional): Wait for the maneuver to complete before continuing with the rest of the program. Defaults to True.
            straight_acceleration (float, optional): The straight acceleration speed in mm/s^2. Values for middle motor: 24-9775 mm/s^2. Defaults to None.
            straight_deceleration (float, optional): The straight deceleration speed in mm/s^2. Values for middle motor: 24-9775 mm/s^2. Defaults to None.
        """
        self.push_and_set_acceleration_deceleration(straight_acceleration, straight_deceleration)
        self.turn(angle)
        self.drive(distance, then=then, wait=wait)
        self.pop_and_set_acceleration_deceleration()

    def turn_to_and_drive(self, angle:float, distance: float, then: Stop = Stop.HOLD, wait: bool=True, straight_acceleration:float=None, straight_deceleration:float=None):
        """Turn to the given angle offset before driving straight.

        Args:
            angle (float, deg): The angle offset to turn to.
            distance (float, mm): The distance to drive.
            then (Stop, optional): What to do after coming to a standstill. Defaults to Stop.HOLD.
            wait (bool, optional): Wait for the maneuver to complete before continuing with the rest of the program. Defaults to True.
            straight_acceleration (float, optional): The straight acceleration speed in mm/s^2. Values for middle motor: 24-9775 mm/s^2. Defaults to None.
            straight_deceleration (float, optional): The straight acceleration speed in mm/s^2. Values for middle motor: 24-9775 mm/s^2. Defaults to None.

        Returns:
            _type_: _description_
        """
        return self.turn_and_drive(angle-self.angle(), distance, then=then, wait=wait, straight_acceleration=straight_acceleration, straight_deceleration=straight_deceleration)

    def straight_ms(self, time_ms:int, speed:float=_DEFAULT_DRIVE_SPEED, then: Stop = Stop.HOLD, straight_acceleration:float=None, straight_deceleration:float=None):
        """Drive straight for the given time in ms with given speed.

        Args:
            time_ms (int, ms): The time in ms to drive straight.
            speed (float, mm/s): The speed to drive
            then (Stop, optional): What to do after coming to a standstill. Defaults to Stop.HOLD.
            straight_acceleration (float, optional): The straight acceleration speed in mm/s^2. Values for middle motor: 24-9775 mm/s^2. Defaults to None.
            straight_deceleration (float, optional): The straight deceleration speed in mm/s^2. Values for middle motor: 24-9775 mm/s^2. Defaults to None.
        """
        self.push_and_set_acceleration_deceleration(straight_acceleration, straight_deceleration)
        self.drive_base.drive(speed, 0)
        wait(time_ms)
        self.drive_base.stop()
        self.pop_and_set_acceleration_deceleration()

    def turn(self, angle:float, then: Stop = Stop.HOLD, wait: bool=True):
        """Turns in place by the given angle (clockwise) and stops

        Args:
            angle (float): Angle of the turn (positive values clockwise)
            then (Stop, optional): What to do after coming to a standstill. Defaults to Stop.HOLD.
            wait (bool, optional): Wait for the maneuver to complete before continuing with the rest of the program. Defaults to True.
        """
        return self.drive_base.turn(angle, then=then, wait=wait)

    def turn_to(self, angle:float, then: Stop = Stop.HOLD, wait: bool=True):
        """Turn to given angle (clockweise).

        Args:
            angle (float): _description_
            then (Stop, optional): What to do after coming to a standstill. Defaults to Stop.HOLD.
            wait (bool, optional): Wait for the maneuver to complete before continuing with the rest of the program. Defaults to True.
        """
        return self.drive_base.turn(angle-self.angle(), then=then, wait=wait)

    def turnToNull(self):
        return self.drive_base.turn(-hub.imu.heading())

    def rotate_forward(self, angle:float, then: Stop = Stop.HOLD, wait: bool=True):
        '''
        Drive along the circle to the right.
        '''
        return self.drive_base.curve(_AXLE_TRACK/2, angle, then=then, wait=wait)
    
    def rotate_to_forward(self, angle:float, then: Stop = Stop.HOLD, wait: bool=True):
        return self.rotate_forward(angle-self.angle(), then=then, wait=wait)

    def rotate_backward(self, angle:float, then: Stop = Stop.HOLD, wait: bool=True):
        return self.drive_base.curve(-_AXLE_TRACK/2, angle, then=then, wait=wait)

    def rotate_to_backward(self, angle:float, then: Stop = Stop.HOLD, wait: bool=True):
        return self.rotate_backward(self.angle()-angle, then=then, wait=wait)

    def drive(self, distance:float, angle:float=0, then: Stop = Stop.HOLD, wait: bool=True, straight_acceleration:float=None, straight_deceleration:float=None):
        if angle != 0:
            self.turn(angle)
        self.push_and_set_acceleration_deceleration(straight_acceleration, straight_deceleration)
        self.straight(distance)
        self.pop_and_set_acceleration_deceleration()

    def reset(self):
        """Reset the angle and distance to 0
        """
        return self.drive_base.reset()

    def stop(self):
        """Stop the drive.
        """
        return self.drive_base.stop()

drive = Drive()
