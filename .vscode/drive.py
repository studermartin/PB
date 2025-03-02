from hub import *
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase

PROFILE = 7 # https://docs.pybricks.com/en/stable/pupdevices/motor.html
AXLE_TRACK = 112

class Drive:
    def __init__(self):
        # https://github.com/pybricks/support/issues/1840
        hub.imu.settings(angular_velocity_threshold=1, acceleration_threshold=1000)

        # hub.imu.settings(heading_correction=361) # only available in latest build

        self.left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, profile=PROFILE)
        self.right_motor = Motor(Port.A, Direction.CLOCKWISE, profile=PROFILE)

        self.drive_base = DriveBase(self.left_motor, self.right_motor, wheel_diameter=56, axle_track=AXLE_TRACK)

        self.drive_base.use_gyro(True)
        self.drive_base.settings(turn_rate=50)


    def wait_for_ready():
        pass # while not hub.imu.ready():
            # wait(200)

    def straigt(self, distance:float, then: Stop = Stop.HOLD, wait: bool=True):
        self.drive_base.straight(distance, then=then, wait=wait)

    def turn(self, angle:float, then: Stop = Stop.HOLD, wait: bool=True):
        self.drive_base.turn(angle, then=then, wait=wait)

    def rotate_forward(self, angle:float, then: Stop = Stop.HOLD, wait: bool=True):
        '''
        Drive along the circle to the right.
        '''
        self.drive_base.curve(AXLE_TRACK/2, angle, then=then, wait=wait)
    
    def rotate_backward(self, angle:float, then: Stop = Stop.HOLD, wait: bool=True):
        self.drive_base.curve(-AXLE_TRACK/2, angle, then=then, wait=wait)

    def drive(self, distance:float, angle:float=0, then: Stop = Stop.HOLD, wait: bool=True):
        if angle != 0:
            self.turn(angle)
        self.straigt(distance)

    def stop(self):
        self.drive_base.stop()

drive = Drive()

# deprecated

class Drehrichtung:
    UHRZEIGERSINN = False
    RECHTS = False
    GEGENUHRZEIGERSINN = True
    LINKS = True

class Raeder:
    LINKS = 0
    RECHTS = 1
    LINKS_UND_RECHTS = 2

async def drehe_auf(winkel: float, richtung_uz: bool = True, raeder: int = Raeder.LINKS_UND_RECHTS, drehgeschwindigkeit: int = 500):
    """Drehe auf den gegebenen Winkel in Richtung rechts (=Gegenuhrzeigersinn) oder links (=Uhrzeigersinn) mit den angegebenen Rädern.

    Parameters
    ----------
    winkel : float
        der Winkel im Bereich (-180, 180]; positiv --> Gegenuhrzeigersinn
    richtung_uz : bool, Optional
        die Richtung, Drehrichtung.UHRZEIGERSINN resp. Drehrichtung.RECHTS oder Drehrichtung.GEGENUHRZEIGERSINN resp. Drehrichtung.LINKS
    raeder : int, Optional
        Raeder.LINKS, Raeder.RECHTS, Raeder.LINKS_UND_RECHTS
    drehgeschwindigkeit: int, Optional
        0 bis 1050
    """

    # Turn?
    if raeder == Raeder.LINKS_UND_RECHTS:
        if richtung_uz:
            drive.turn(-winkel)
        else:
            drive.turn(winkel)
    else:
        if raeder == Raeder.LINKS:
            if richtung_uz:
                drive.rotate_forward(winkel)
            else:
                drive.rotate_backward(winkel)
        else:
            # reader == Raeder.RECHTS:
            if richtung_uz:
                drive.rotate_backward(-winkel)
            else:
                drive.rotate_forward(-winkel)



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

        





