import umath
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub

# Aus dem Winkel in Grad muss die Strecke berechnet werden.
# Der Radius des Rades ist 7.5 mm.
VERTICAL_RADIUS = 7.8
VERTIKAL_WINKEL2STRECKE = 2.0*umath.pi*VERTICAL_RADIUS/360    # mm/deg 
VERTIKALE_GESCHWINDIGKEIT = 1/VERTIKAL_WINKEL2STRECKE # deg/mm
VERTICAL_STANDARD_GESCHWINDIGKEIT = 30*VERTIKALE_GESCHWINDIGKEIT    # deg/mm

HORIZONTAL_RADIUS = 10.2
HORIZONTAL_WINKEL2STRECKE = 2.0*umath.pi*HORIZONTAL_RADIUS/360    # mm/deg 
HORIZONTAL_GESCHWINDIGKEIT = 1/HORIZONTAL_WINKEL2STRECKE # deg/mm
HORIZONTAL_STANDARD_GESCHWINDIGKEIT = 50*HORIZONTAL_GESCHWINDIGKEIT    # deg/mm


class Wall:

    def __init__(self):
        self.motor_vertical = Motor(Port.D, Direction.COUNTERCLOCKWISE)
        self.motor_horizontal = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.reset_pos()

    def reset_pos(self):
        self.motor_vertical.reset_angle(0)
        self.motor_horizontal.reset_angle(0)

    def up(self, distance:float, wait:bool=True):
        self.motor_vertical.run_angle(VERTICAL_STANDARD_GESCHWINDIGKEIT, distance/VERTIKAL_WINKEL2STRECKE, wait=wait)

    def upTo(self,distance:float, wait:bool=True):
        self.motor_vertical.run_target(VERTICAL_STANDARD_GESCHWINDIGKEIT, distance/VERTIKAL_WINKEL2STRECKE, wait=wait)

    def left(self, distance, wait:bool=True):
        self.motor_horizontal.run_angle(HORIZONTAL_STANDARD_GESCHWINDIGKEIT, distance/HORIZONTAL_WINKEL2STRECKE, wait=wait)

    def leftTo(self, distance:float, wait:bool=True):
        self.motor_horizontal.run_target(HORIZONTAL_STANDARD_GESCHWINDIGKEIT, distance/HORIZONTAL_WINKEL2STRECKE, wait=wait)

    def right(self, distance, wait:bool=True):
        self.left(-distance, wait=wait)

    def rightTo(self, distance, wait:bool=True):
        self.leftTo(-distance, wait=wait)

wall = Wall()

# deprecated

def wand_initialisieren():
    wall.reset_pos()

def ausführen_wand_vertikal(distance_cm:float):
    wall.upTo(10*distance_cm)

def start_wand_vertikal(distance_cm:float):
    wall.upTo(10*distance_cm, wait=False)

def ausführen_wand_horizontal(distance_cm:float):
    wall.leftTo(10*distance_cm)
