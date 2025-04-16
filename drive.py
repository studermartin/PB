from hub import hub, wait
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase

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
        self.drive_base.settings(turn_rate=50)
        self.drive_base.settings(straight_speed=400)

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
        self.turn_and_drive(angle-self.angle(), distance, then=then, wait=wait)

    def straight_ms(self, time_ms:int, speed:float, then: Stop = Stop.HOLD):
        self.drive_base.drive(speed, 0)
        wait(time_ms)
        self.drive_base.stop()

    def turn(self, angle:float, then: Stop = Stop.HOLD, wait: bool=True):
        self.drive_base.turn(angle, then=then, wait=wait)

    def turn_to(self, angle:float, then: Stop = Stop.HOLD, wait: bool=True):
        """Turn to given angle (clockweise).

        Args:
            angle (float): _description_
            then (Stop, optional): _description_. Defaults to Stop.HOLD.
            wait (bool, optional): _description_. Defaults to True.

        Returns:
            _type_: _description_
        """
        return self.drive_base.turn(angle-self.angle(), then=then, wait=wait)

    def turnToNull(self):
        self.drive_base.turn(-hub.imu.heading())

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
        self.straight(distance)

    def reset(self):
        """Reset the angle and distance to 0
        """
        return self.drive_base.reset()

    def stop(self):
        """Stop the drive.
        """
        return self.drive_base.stop()

drive = Drive()
