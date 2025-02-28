from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

hub = PrimeHub()

motor_vertical = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_horizontal = Motor(Port.B, Direction.COUNTERCLOCKWISE)

WAND_CM2WINKELVERTIKAL = -74
WAND_CM2WINKELSEITLICH = 74


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
