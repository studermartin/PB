from pybricks.tools import wait
from drive import drive
from hub import wait_for_button_pressed
from wall import wall

def run5():
    wall.upTo(45, wait=False)
    drive.drive_to(648, 0)
    drive.rotate_to_backward(42)
    drive.drive_to(130, 44)
    drive.straight_ms(3)
    wall.rightTo(-10)
    wall.upTo(55)
    drive.drive_to(-155, 44)
    drive.rotate_to_backward(0)
    drive.drive_to(15, 0, speed=110)
    wall.rightTo(77, wait=False)
    drive.rotate_to_forward(-88)
    drive.drive_to(50, -90, speed=190)
    wall.upTo(15)
    drive.drive_to(-50, -90, speed=190)
    wall.rightTo(2)
    drive.drive_to(70, -90, speed=190)
    wall.rightTo(70)
    wall.upTo(30)
    wall.upTo(15, speed=20, wait=False)
    drive.drive_to(315, -88)
    wall.upTo(75)
    wait(1000)
    wall.rightTo(10)
    wall.upTo(65)
    wall.rightTo(10)
