from pybricks.tools import wait
from pybricks.parameters import Stop
from drive import drive
from hub import wait_for_button_pressed
from wall import wall

def run1():



    wall.rightTo(-70, wait=False)
    drive.drive_to(333, 0)
    wall.rightTo(-10, 300, wait=False)
    drive.drive_to(138, 0)
    wait(20)
    wall.rightTo(15)
    wall.upTo(50)
    wall.rightTo(26)
    wait_for_button_pressed()
    wall.rightTo(55, wait=False)
    wall.upTo(72)
    wait(20)
    drive.drive_to(-75, 0, 195)
    wall.rightTo(-20, wait=False)
    wall.upTo(10)
    wall.rightTo(-65, 190, wait=False)
    drive.drive_to(210, 0, 300)
    wall.rightTo(20)
    drive.drive_to(90, 0, 190)
    wall.upTo(0, wait=False)
    wall.rightTo(-10)
    drive.drive_to(-125, 0)
    wall.rightTo(72)
    wall.rightTo(20)
    wall.rightTo(0, wait=False)
    drive.drive_to(-350, 0)
    drive.rotate_to_backward(-45)
    drive.drive_to(260, -45)
    drive.straight_ms(400, 160)
    wait(200)
    drive.drive_to(-400, -50)
    drive.turn(0)

