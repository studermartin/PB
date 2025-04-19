from umath import sqrt, fabs, copysign
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from hub import hub, wait

PROFILE = None # values from 5 (smallest values for the motors used) up to at least 100 (https://docs.pybricks.com/en/stable/pupdevices/motor.html)
AXLE_TRACK = 140 

class Drive:
    def __init__(self):
        # https://github.com/pybricks/support/issues/1840
        hub.imu.settings(angular_velocity_threshold=1, acceleration_threshold=1000)

        # hub.imu.settings(heading_correction=361) # only available in latest build

        self.left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE, profile=PROFILE)
        self.right_motor =Motor(Port.B, Direction.CLOCKWISE, profile=PROFILE)

        self.drive_base = DriveBase(self.left_motor, self.right_motor, wheel_diameter=56, axle_track=AXLE_TRACK)

        self.drive_base.use_gyro(True)
        self.drive_base.settings(turn_rate=40)
        self.drive_base.settings(straight_speed=400)

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
    def drive_to(self, distance:float, target_angle:float=0.0, straight_speed:float=None, then: Stop = Stop.HOLD):
        """Drive distance forward/backward to given target angle.
        The target angle should not deviate to much from the current angle. If so consider a turn first. 

        Args:
            distance (float): Distance in mm. Positive values to drive foward, negative value to drive backward.
            target_angle (float, optional): Target angle. Defaults to 0.0.
            straight_speed (float, optional): Straight speed. Defaults to default straight speed.
            then (Stop, optional): What to do after coming to a standstill. Defaults to Stop.HOLD.
        """
        loop_time = 5  # time per loop in milliseconds        
        target_distance = distance # target distance
        target_speed = straight_speed if straight_speed is not None else self.get_straight_speed() # target speed of robot in mm/s
        k_p = 5 #  3 # the Constant 'K' for the 'p' proportional controller

        integral = 0 # initialize
        k_i = 0.06 # 0.025 #  the Constant 'K' for the 'i' integral term

        derivative = 0 # initialize
        lastError = 0 # initialize
        k_d = 37.5 # 3 #  the Constant 'K' for the 'd' derivative term

        start_distance = self.drive_base.distance()
        delta_from_start = self.drive_base.distance()-start_distance    # if the robot drives backward, self.drive_base.distance() yields negative values
        delta_distance = fabs(target_distance)-fabs(delta_from_start)

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

        # to implement the "then"
        self.drive_base.straight(0,then)         

    def wait_for_ready():
        pass # while not hub.imu.ready():
            # wait(200)

    def angle(self)->float:
        """Get the angle of the drive base.

        Returns:
            float: accumulated angle since last reset.
        """
        return self.drive_base.angle()

    def straight(self, distance:float, then: Stop = Stop.HOLD, wait: bool=True):
        return self.drive_base.straight(distance, then=then, wait=wait)

    def turn_and_drive(self, angle:float, distance: float, then: Stop = Stop.HOLD, wait: bool=True):
        self.turn(angle)
        return self.drive(distance, then=then, wait=wait)

    def turn_to_and_drive(self, angle:float, distance: float, then: Stop = Stop.HOLD, wait: bool=True):
        return self.turn_and_drive(angle-self.angle(), distance, then=then, wait=wait)

    def straight_ms(self, time_ms:int, speed:float, then: Stop = Stop.HOLD):
        self.drive_base.drive(speed, 0)
        wait(time_ms)
        self.drive_base.stop()

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
        return self.drive_base.curve(AXLE_TRACK/2, angle, then=then, wait=wait)
    
    def rotate_to_forward(self, angle:float, then: Stop = Stop.HOLD, wait: bool=True):
        return self.rotate_forward(angle-self.angle(), then=then, wait=wait)

    def rotate_backward(self, angle:float, then: Stop = Stop.HOLD, wait: bool=True):
        return self.drive_base.curve(-AXLE_TRACK/2, angle, then=then, wait=wait)

    def rotate_to_backward(self, angle:float, then: Stop = Stop.HOLD, wait: bool=True):
        return self.rotate_backward(self.angle()-angle, then=then, wait=wait)

    def drive(self, distance:float, angle:float=0, then: Stop = Stop.HOLD, wait: bool=True):
        if angle != 0:
            self.turn(angle)
        return self.straight(distance)

    def reset(self):
        """Reset the angle and distance to 0
        """
        return self.drive_base.reset()

    def stop(self):
        """Stop the drive.
        """
        return self.drive_base.stop()

drive = Drive()
