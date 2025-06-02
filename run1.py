from pybricks.tools import wait
from pybricks.parameters import Stop
from drive import drive
from hub import wait_for_button_pressed
from wall import wall

def run1():


    wall.upTo(30, speed=150, wait=False)
    wall.rightTo(-40, speed=150, wait=False)
    drive.drive_to(610, 0, speed=600)
    #wall.upTo(0, wait=False)
    wall.rightTo(75, speed=200)
    wall.rightTo(50, speed=200)
    #wall.upTo(30)
    drive.drive_to(70, 0, speed=600)
    wall.rightTo(-40, speed=450, wait=False)
    wall.upTo(0)
    drive.drive_to(-370, 0, speed=600)
    drive.rotate_to_backward(-45)
    drive.drive_to(150, -45, speed=600)
    drive.straight_ms(500, 150)
    wait(400)
    drive.drive_to(-160, -45, speed=600)
    wall.rightTo(0, speed=150, wait=False)
    # drive.drive_base.arc(-350, distance=-270)
    drive.arc(-350, distance=-270)
    drive.stop()