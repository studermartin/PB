from pybricks.tools import wait
from drive import drive
from wall import wall

def run5():
    drive.drive_to(920,0)
    wait(100)
    drive.drive_to(-50,0,speed=190)
    wall.upTo(55, 10)
    drive.drive_to(-110, 0, speed=190)
    wall.upTo(100)
    drive.drive_to(-250,0)
    wall.rightTo(0, wait=False)
    wall.upTo(100, wait=False)
    drive.rotate_to_forward(-14)
    drive.drive_to(420, -14)
    drive.rotate_to_backward(15)
    drive.drive_to(750, -15)
    wall.upTo(10)
    
