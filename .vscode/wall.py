import umath
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Color
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from fll import *

# Aus dem Winkel in Grad muss die Strecke berechnet werden.
# Der Radius des Rades ist 7.5 mm.
VERTICAL_RADIUS = 7.8
VERTIKAL_WINKEL2STRECKE = 2.0*umath.pi*VERTICAL_RADIUS/360    # mm/deg 
VERTIKALE_GESCHWINDIGKEIT = 1/VERTIKAL_WINKEL2STRECKE # deg/mm
VERTICAL_STANDARD_GESCHWINDIGKEIT = 40*VERTIKALE_GESCHWINDIGKEIT    # deg/mm

HORIZONTAL_RADIUS:float = 10.2
HORIZONTAL_WINKEL2STRECKE = 2.0*umath.pi*HORIZONTAL_RADIUS/360    # mm/deg 
HORIZONTAL_GESCHWINDIGKEIT = 1/HORIZONTAL_WINKEL2STRECKE # deg/mm
HORIZONTAL_STANDARD_GESCHWINDIGKEIT = 50*HORIZONTAL_GESCHWINDIGKEIT    # deg/mm

WAND_HORIZONTAL_HELLIGKEIT_GRENZE_ORANGE_WEISS = 38
WAND_HORIZONTAL_HELLIGKEIT_GRENZE_SCHWARZ_ORANGE = 15

class Wall:

    def __init__(self):
        self.motor_vertical = Motor(Port.D, Direction.CLOCKWISE)
        self.motor_horizontal = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.color_sensor = ColorSensor(Port.F)
        self.reset_pos()

    def reset_pos(self):
        self.motor_vertical.reset_angle(0)
        self.motor_horizontal.reset_angle(0)

    def up(self, distance:float, speed: float=VERTICAL_STANDARD_GESCHWINDIGKEIT, wait:bool=True):
        self.motor_vertical.run_angle(speed, distance/VERTIKAL_WINKEL2STRECKE, wait=wait)

    def upTo(self,distance:float, speed: float=VERTICAL_STANDARD_GESCHWINDIGKEIT, wait:bool=True):
        self.motor_vertical.run_target(speed, distance/VERTIKAL_WINKEL2STRECKE, wait=wait)

    def left(self, distance:float=None, speed: float=HORIZONTAL_STANDARD_GESCHWINDIGKEIT, wait:bool=True):
        if distance != None:
            self.motor_horizontal.run_angle(speed, distance/HORIZONTAL_WINKEL2STRECKE, wait=wait)
        else:
            self.motor_horizontal.run(speed)

    def leftTo(self, distance:float, speed: float=HORIZONTAL_STANDARD_GESCHWINDIGKEIT, wait:bool=True):
        self.motor_horizontal.run_target(speed, distance/HORIZONTAL_WINKEL2STRECKE, wait=wait)

    def right(self, distance:float=None, speed: float=HORIZONTAL_STANDARD_GESCHWINDIGKEIT, wait:bool=True):
        if distance != None:
            self.motor_horizontal.run_angle(-speed, distance/HORIZONTAL_WINKEL2STRECKE, wait=wait)
        else:
            self.motor_horizontal.run(-speed)

    def rightTo(self, distance:float, speed: float=HORIZONTAL_STANDARD_GESCHWINDIGKEIT, wait:bool=True):
        self.leftTo(-distance, speed=speed, wait=wait)

    def stop(self):
        self.motor_vertical.stop()

    def downToStop(self):
        self.motor_vertical.run(-VERTICAL_STANDARD_GESCHWINDIGKEIT)
        
        while not self.motor_vertical.stalled():
            wait(10)
        self.stop()


    def wand_horizontal_ausrichten_neu_farbe(self):
        reflection = self.color_sensor.reflection()
        if reflection>WAND_HORIZONTAL_HELLIGKEIT_GRENZE_ORANGE_WEISS:
            return Color.WHITE
        elif reflection>WAND_HORIZONTAL_HELLIGKEIT_GRENZE_SCHWARZ_ORANGE:
            return Color.ORANGE
        else:
            return Color.BLACK

    def wand_horizontal_ausrichten_neu_farbcodierung(self, reflection: int):
        if reflection==Color.WHITE:
            return "Weiss"
        elif reflection==Color.ORANGE:
            return "Orange"
        else:
            return "Schwarz"


    def center(self):
        beepHigh()
        DEBUG=True

        if DEBUG:
            print("Start: wand_horizontal_ausrichten_neu")
            print(self.color_sensor.reflection())

        # Ausrichtung über den Reflexionssensor bestimmen
        start_farbe = self.wand_horizontal_ausrichten_neu_farbe()
        if DEBUG:
            print("Startfarbe: ", self.wand_horizontal_ausrichten_neu_farbcodierung(start_farbe))
        
        if start_farbe == Color.ORANGE:
            self.right()
        elif start_farbe == Color.BLACK:
            self.left()
        else:
            # Ist die Wand ein wenig verschoben, so dass die Hälfte weiss, die andere Hälfte Orange ist, wird trotzdem schon ein Reflexionswert von 99 zurückgegeben.
            # Deshalb die Wand zuerst verschieben.
            self.right(20)
            self.left()
            start_farbe = Color.BLACK
                
        farbe = start_farbe
        while farbe != Color.WHITE:
            farbe = self.wand_horizontal_ausrichten_neu_farbe()
            wait(5)
            if DEBUG:
                pass
                # print("Reflection:", self.wand_horizontal_ausrichten_neu_farbcodierung(farbe))
        if start_farbe == Color.ORANGE:
            # Auf der orangen Seite liefert die Reflexion bereits eine Reflexionswerte für Weiss, wenn die Hälfte Orange, die andere Hälfte Weiss ist. 
            # Deshalb einfach ein wenig weiterlaufen lassen.
            wait(0)
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
