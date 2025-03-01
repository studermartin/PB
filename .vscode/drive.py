from hub import *
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase

class Drive:
    def __init__(self):
        # https://github.com/pybricks/support/issues/1840
        hub.imu.settings(angular_velocity_threshold=1, acceleration_threshold=1000)

        # hub.imu.settings(heading_correction=361) # only available in latest


        self.left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.A, Direction.CLOCKWISE)

        self.drive_base = DriveBase(self.left_motor, self.right_motor, wheel_diameter=56, axle_track=112)

        self.drive_base.use_gyro(True)
        self.drive_base.settings(turn_rate=50)



    def wait_for_ready():
        pass # while not hub.imu.ready():
            # wait(200)


drive = Drive()

# deprecated



