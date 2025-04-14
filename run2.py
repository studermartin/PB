from pybricks.tools import wait
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import *
from pybricks import version
from drive import *
from fll import *
from hub import *

def run2():
    # wall.leftTo(-5*10, wait=False)
    # wall.upTo(0, wait=False)

    wait_for_button_pressed()

    # wall.leftTo(0, wait=False)
    # wall.upTo(8*10, wait=False)
    drive.straigt(400)

    # wall.leftTo(7*10)

