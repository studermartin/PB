import umath
from pybricks.tools import wait
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Color

from fll import beepHigh, beepLow

# Aus dem Winkel in Grad muss die Strecke berechnet werden.
# Der Radius des Rades ist 7.5 mm.
VERTICAL_RADIUS = 7.95
VERTIKAL_WINKEL2STRECKE = 2.0*umath.pi*VERTICAL_RADIUS/360    # mm/deg 
VERTIKALE_GESCHWINDIGKEIT = 1/VERTIKAL_WINKEL2STRECKE # deg/mm
VERTICAL_STANDARD_GESCHWINDIGKEIT = 40*VERTIKALE_GESCHWINDIGKEIT    # deg/mm

HORIZONTAL_RADIUS:float = 10.0
HORIZONTAL_WINKEL2STRECKE = 2.0*umath.pi*HORIZONTAL_RADIUS/360    # mm/deg 
HORIZONTAL_GESCHWINDIGKEIT = 1/HORIZONTAL_WINKEL2STRECKE # deg/mm
HORIZONTAL_DEFAULT_SPEED = 50*HORIZONTAL_GESCHWINDIGKEIT    # deg/mm

WAND_HORIZONTAL_BRIGHTNESS_BOUNDARY_ORANGE_WHITE = 70
WAND_HORIZONTAL_HELLIGKEIT_GRENZE_SCHWARZ_ORANGE = 15

class Wall:

    def __init__(self):
        self.motor_horizontal = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.motor_vertical = Motor(Port.D, Direction.COUNTERCLOCKWISE)

        self.color_sensor = ColorSensor(Port.E)
        self.reset_pos()

    def reset_pos(self):
        self.motor_vertical.reset_angle(0)
        self.motor_horizontal.reset_angle(0)

    def up(self, distance:float, speed: float=VERTICAL_STANDARD_GESCHWINDIGKEIT, wait:bool=True):
        return self.motor_vertical.run_angle(speed, distance/VERTIKAL_WINKEL2STRECKE, wait=wait)

    def upTo(self,distance:float, speed: float=VERTICAL_STANDARD_GESCHWINDIGKEIT, wait:bool=True):
        return self.motor_vertical.run_target(speed, distance/VERTIKAL_WINKEL2STRECKE, wait=wait)

    def left(self, distance:float=None, speed: float=HORIZONTAL_DEFAULT_SPEED, wait:bool=True):
        if distance is not None:
            self.motor_horizontal.run_angle(speed, distance/HORIZONTAL_WINKEL2STRECKE, wait=wait)
        else:
            self.motor_horizontal.run(speed)

    def leftTo(self, distance:float, speed: float=HORIZONTAL_DEFAULT_SPEED, wait:bool=True):
        return self.motor_horizontal.run_target(speed, distance/HORIZONTAL_WINKEL2STRECKE, wait=wait)

    def right(self, distance:float=None, speed: float=HORIZONTAL_DEFAULT_SPEED, wait:bool=True):
        if distance is not None:
            return self.motor_horizontal.run_angle(-speed, distance/HORIZONTAL_WINKEL2STRECKE, wait=wait)
        else:
            return self.motor_horizontal.run(-speed)

    def rightTo(self, distance:float, speed: float=HORIZONTAL_DEFAULT_SPEED, wait:bool=True):
        self.leftTo(-distance, speed=speed, wait=wait)

    def stop(self):
        self.motor_vertical.stop()
        self.motor_horizontal.stop()

    def downToStop(self):
        self.motor_vertical.run(-VERTICAL_STANDARD_GESCHWINDIGKEIT)
        
        while not self.motor_vertical.stalled():
            wait(10)
        self.stop()

    def center_reflection(self):
        return self.color_sensor.reflection()

    def center_color(self):
        reflection = self.center_reflection()
        if reflection>WAND_HORIZONTAL_BRIGHTNESS_BOUNDARY_ORANGE_WHITE:
            return Color.WHITE
        elif reflection>WAND_HORIZONTAL_HELLIGKEIT_GRENZE_SCHWARZ_ORANGE:
            return Color.ORANGE
        else:
            return Color.BLACK

    def center_color_coding(self, reflection: int):
        if reflection==Color.WHITE:
            return "WHITE"
        elif reflection==Color.ORANGE:
            return "ORANGE"
        else:
            return "BLACK"


    def center(self, speed=HORIZONTAL_DEFAULT_SPEED):
        beepHigh()
        DEBUG=True

        if DEBUG:
            print("Start: wand_horizontal_ausrichten_neu")
            print(self.color_sensor.reflection())

        # Ausrichtung über den Reflexionssensor bestimmen
        initial_color = self.center_color()
        if DEBUG:
            print("Startfarbe: ", self.center_color_coding(initial_color))
        
        if initial_color == Color.ORANGE:
            self.right(speed=speed)
        elif initial_color == Color.BLACK:
            self.left(speed=speed)
        else:
            # Ist die Wand ein wenig verschoben, so dass die Hälfte weiss, die andere Hälfte Orange ist, wird trotzdem schon ein Reflexionswert von 99 zurückgegeben.
            # Deshalb die Wand zuerst verschieben.
            self.right(speed=speed)
            self.left(speed=speed)
            initial_color = Color.BLACK
                
        color = initial_color
        while color != Color.WHITE:
            color = self.center_color()
            wait(5)
            if DEBUG:
                print("Reflection:", self.center_color_coding(color))
        if initial_color == Color.ORANGE:
            # Auf der orangen Seite liefert die Reflexion bereits eine Reflexionswerte für Weiss, wenn die Hälfte Orange, die andere Hälfte Weiss ist. 
            # Deshalb einfach ein wenig weiterlaufen lassen.
            wait(50)
        elif initial_color == Color.BLACK:
            wait(35)
        self.stop()
        beepLow()
        if DEBUG:
            print("Ende: wand_horizontal_ausrichten_neu")


wall = Wall()

# deprecated

def wand_initialisieren():
    wall.reset_pos()

async def ausführen_wand_vertikal(distance_cm:float):
    wall.upTo(10*distance_cm)

def start_wand_vertikal(distance_cm:float):
    wall.upTo(10*distance_cm, wait=False)

async def ausführen_wand_horizontal(distance_cm:float):
    wall.leftTo(10*distance_cm)

async def ausführen_wand_seitlich(distance_cm:float):
    wall.leftTo(10*distance_cm)

def start_wand_seitlich(distance_cm:float):
    wall.leftTo(10*distance_cm, wait=False)
