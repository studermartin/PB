import umath
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub

hub = PrimeHub()

# Aus dem Winkel in Grad muss die Strecke berechnet werden.
# Der Radius des Rades ist 7.5 mm.
VERTICAL_RADIUS = 7.8
VERTIKAL_WINKEL2STRECKE = 2*umath.pi/360*VERTICAL_RADIUS    # mm/deg 
VERTIKALE_GESCHWINDIGKEIT = 1/VERTIKAL_WINKEL2STRECKE # deg/mm
VERTICAL_STANDARD_GESCHWINDIGKEIT = 30*VERTIKALE_GESCHWINDIGKEIT    # deg/mm

HORIZONTAL_RADIUS = 1.0
HORIZONTAL_WINKEL2STRECKE = 2*umath.pi/360*HORIZONTAL_RADIUS    # mm/deg 
HORIZONTAL_GESCHWINDIGKEIT = 1/HORIZONTAL_WINKEL2STRECKE # deg/mm
HORIZONTAL_STANDARD_GESCHWINDIGKEIT = 30*HORIZONTAL_GESCHWINDIGKEIT    # deg/mm


class Wall:

    def __init__(self):
        self.motor_vertical = Motor(Port.D, Direction.COUNTERCLOCKWISE)
        self.motor_horizontal = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.reset_pos()

    def reset_pos(self):
        self.motor_vertical.reset_angle(0)
        self.motor_horizontal.reset_angle(0)

    def up(self, distance:float, VERTIKAL_WINKEL2STRECKE:float, wait:bool=True):
        # print("Angle: ", self.motor_vertical.angle())

        self.motor_vertical.run_angle(VERTICAL_STANDARD_GESCHWINDIGKEIT, distance/VERTIKAL_WINKEL2STRECKE, wait=wait)

        # print("Angle: ", self.motor_vertical.angle())

    def upTo(self,distance:float, wait:bool=True):
        # print("Angle: ", self.motor_vertical.angle())

        self.motor_vertical.run_target(VERTICAL_STANDARD_GESCHWINDIGKEIT, distance/VERTIKAL_WINKEL2STRECKE, wait=wait)
    
        # print("Angle: ", self.motor_vertical.angle())


    def left(self, distance):
        self.motor_horizontal.run_angle(HORIZONTAL_STANDARD_GESCHWINDIGKEIT, distance/HORIZONTAL_WINKEL2STRECKE)




wall = Wall()

def ausführen_wand_vertikal(self, distance_cm):
    wall.up(VERTICAL_STANDARD_GESCHWINDIGKEIT, 10*distance_cm)

def start_wand_vertikal(self, distance_cm):
    wall.up(VERTICAL_STANDARD_GESCHWINDIGKEIT, 10*distance_cm, wait=False)

def ausführen_wand_horizontal(self, distance_cm):
    wall.left(VERTICAL_STANDARD_GESCHWINDIGKEIT, 10*distance_cm)


wait(1000)
wand.upTo(20, wait=False)
hub.speaker.beep(500)
wand.upTo(20)
hub.speaker.beep(500)
wand.upTo(40)
hub.speaker.beep(500)
wand.upTo(40)

# wand.up(10)
# wand.up(10)
# wand.left(40)




'''
wand_startposition_vertikal_cm = 0.0

async def wand_vertikal_ausrichten():
    motor.reset_relative_position(port.A, 0)
    await motor.run_to_relative_position(port.A, -200, -400) # ein bisschen nach oben, dass, falls er zu Beginn ganz unten steht, den Schwung hat, um den Roboter zu lupfen
    motor.run(port.A, 330)
    while True:
        if getRollwinkel() > 2:
            break
    motor.stop(port.A)
    beepLow()
    await warte(400)
    motor.run(port.A, -100)
    while True:
        if getRollwinkel() < 0.3:
            break
    motor.stop(port.A)
    beepLow()
    wand_startposition_vertikal(-0.2)

async def wand_horizontal_ausrichten_von_rechts_nach_links():
    # wand langsam nach rechts zum einhängen
    motor.reset_relative_position(port.B, 0)
    motor.run(port.B, -400) # fahre nach links
    
    # fahren bis Reflexion >= 2 (Start Konstruktion der Wand)
    while color_sensor.reflection(port.F)<2:
        await runloop.sleep_ms(1)
        if DEBUG:
            print("Sensorwert:", color_sensor.reflection(port.F))
            await warte(DEBUG_PRINT_WAITING_TIME_MS)

    beepLow()

    # fahren bis Reflexino >= 10 (Aufbau erkannt)
    # Alternativ:
    # color_sensor.color(port.A) == color.RED
    while color_sensor.reflection(port.F)<60:
        await runloop.sleep_ms(1)
        if DEBUG:
            print("Sensorwert:", color_sensor.reflection(port.F))
            await warte(DEBUG_PRINT_WAITING_TIME_MS)
    # await warte(5)
    # motor.run_to_relative_position(port.B, 10, -200)
    await warte(20)
    motor.stop(port.B)
    motor.reset_relative_position(port.B, 0)
    beepHigh()

def wand_startposition_vertikal(position:float):
    """ Setze die relative Startposition.

    Parameters
    ----------
    position : float
        die Position in cm

    """
    global wand_startposition_vertikal_cm

    wand_startposition_vertikal_cm = position

def wand_initialisieren(winkel: int = 0):
    print("Initialisiere Wand")
    motor_horizontal.reset_angle(winkel)
    motor_vertical.reset_angle(winkel)
    wand_startposition_vertikal(0)

def start_wand_vertikal(cm: float, geschwindigkeit:int=1000):
    """Wand auf gegebenen Position heben/senken.

    Parameters
    ----------
    cm : float
        die Position in cm
    geschwindigkeit: int
        0 ... 1050
    """
    global wand_startposition_vertikal_cm

    # motor_vertical.run_to_relative_position(port.A, int((cm-wand_startposition_vertikal_cm)*WAND_CM2WINKELVERTIKAL), geschwindigkeit, stop=motor.HOLD)

async def ausführen_wand_vertikal(cm, geschwindigkeit=1000):
    """Wand auf gegebenen Position heben/senken.

    Parameters
    ----------
    cm : float
        die Position in cm
    geschwindigkeit : int, Optional
        die Geschwindigkeit im Bereich 0 - 1050 (grosser Motor)
    """
    await motor.run_to_relative_position(port.A, int((cm-wand_startposition_vertikal_cm)*WAND_CM2WINKELVERTIKAL), geschwindigkeit, stop=motor.HOLD)


def start_wand_seitlich(cm: float, geschwindigkeit:int = 1000):
    """Wand auf gegebenen Position nach rechts verschieben.

    Parameters
    ----------
    cm : float
        die Position in cm nach rechts; negative Werte nach links; -10.0 bis 10.0
    geschwindigkeit: int
        0 bis 1050
    """

    print("Starte Wand seitlich ")
    motor.run_to_relative_position(port.B, int(cm*WAND_CM2WINKELSEITLICH), geschwindigkeit, stop=motor.HOLD)


async def ausführen_wand_seitlich(cm: float):
    """Wand auf gegebenen Position nach rechts verschieben.

    Parameters
    ----------
    cm : float
        die Position in cm nach rechts; negative Werte nach links; -10.0 bis 10.0
    """
    await motor.run_to_relative_position(port.B, int(cm*WAND_CM2WINKELSEITLICH), 1000, stop=motor.HOLD)
'''