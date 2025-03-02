from hub import *
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase

PROFILE = 7 # https://docs.pybricks.com/en/stable/pupdevices/motor.html

class Drive:
    def __init__(self):
        # https://github.com/pybricks/support/issues/1840
        hub.imu.settings(angular_velocity_threshold=1, acceleration_threshold=1000)

        # hub.imu.settings(heading_correction=361) # only available in latest build

        self.left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, profile=PROFILE)
        self.right_motor = Motor(Port.A, Direction.CLOCKWISE, profile=PROFILE)

        self.drive_base = DriveBase(self.left_motor, self.right_motor, wheel_diameter=56, axle_track=112)

        self.drive_base.use_gyro(True)
        self.drive_base.settings(turn_rate=50)


    def wait_for_ready():
        pass # while not hub.imu.ready():
            # wait(200)

    def straigt(self, distance:float, then: Stop = Stop.HOLD, wait: bool=True):
        self.drive_base.straight(distance, then=then, wait=wait)

    def turn(self, angle:float, then: Stop = Stop.HOLD, wait: bool=True):
        self.drive_base.turn(angle, then=then, wait=wait)

    def stop(self):
        self.drive_base.stop()

drive = Drive()

# deprecated

async def gyro_fahren(strecke_cm: float, tempo: int=500, winkel: float=0, beschleunigung:int = 1000):
    """ Fahre mit Gyro die angegebene Strecke in cm vorwärts oder rückwärts.

    Parameters
    ----------
    strecke_cm: float
        die zu fahrende Strecke in cm; positiver Wert für vorwärts, negativer Wert für rückwärts
    tempo : int
        die Geschwindigkeit im Bereich 0 - 1050 (grosser Motor)
    winkel : float
        der Winkel im Bereich (-180, 180]; positiv im Gegenuhrzeigersinn; der Winkel sollte nicht allzustark von der aktuellen Ausrichtung abweichen
    beschleunigung : int
        0 ... 10000, Standard 1000

    """
    if winkel != 0:
        drive.turn(winkel)

    # tempo und beschleinigung werden ignoriert

    drive.straigt(10*strecke_cm)


async def gyro_fahren_timeout(strecke_cm: float, tempo: int=500, winkel: float=0, beschleunigung:int = 1000):
    """ Fahre mit Gyro die angegebene Strecke in cm vorwärts oder rückwärts.
    Falls sich der Roboter eine gewisse Zeit nicht mehr bewegt (Räder bewegen sich nicht, drehen also nicht durch), wird der Block beendet.

    Parameters
    ----------
    strecke_cm: float
        die zu fahrende Strecke in cm; positiver Wert für vorwärts, negativer Wert für rückwärts
    tempo : int
        die Geschwindigkeit im Bereich 0 - 1050 (grosser Motor)
    winkel : float
        der Winkel im Bereich (-180, 180]; positiv im Gegenuhrzeigersinn; der Winkel sollte nicht allzustark von der aktuellen Ausrichtung abweichen
    beschleunigung : int
        0 ... 10000, Standard 1000

    """
    if winkel != 0:
        drive.turn(winkel)

    # tempo und beschleinigung werden ignoriert

    drive.straigt(10*strecke_cm, wait=True)

    while not drive.drive_base.done():
        if drive.drive_base.stalled():
            drive.stop()
            return
        wait(10)

        





