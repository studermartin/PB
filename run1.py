from pybricks.tools import wait
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import *
from pybricks import version
from drive import *
from fll import *
from hub import *
from wall import *

def run1():
    
    # Artifical habitat
    wait(500)
    wall.upTo(15)
    wait_for_button_pressed()
    wall.leftTo(20)
    wait(500)
    wall.leftTo(-5)
    drive.turnToNull()

    drive.straigt(150, then=Stop.COAST)
    # ToDo: Die Wand soll sich während dem Fahren bewegen. Man müsste also 2 Sekunden oder so warten
    wall.leftTo(15, wait=False)
    drive.straigt(255)

run1()
