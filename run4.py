from pybricks.tools import wait
from pybricks.parameters import Stop
from drive import drive
from hub import wait_for_button_pressed
from wall import wall

def run4():

    wall.upTo(5)
    wall.rightTo(55)
    wait_for_button_pressed()

    wall.rightTo(-20)
    wall.rightTo(20)
    drive.drive_to(0, 555)
    wait(50)
    wall.rightTo(30, wait=False)
    drive.rotate_to_forward(-49)

    wall.upTo(120)
    drive.drive_to(-50, 78)

    wall.upTo(35)
    drive.straight_ms(200, 200)
    wall.upTo(0)
    wait(200)
    wall.upTo(110)
    drive.drive_to(-50, -64)
    wall.upTo(43, wait=False)
    drive.rotate_backward(0)
    wall.rightTo(50, wait=False)
    drive.drive_to(0, -610)
    
