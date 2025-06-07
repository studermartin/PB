from pybricks.tools import wait
from drive import drive
from hub import wait_for_button_pressed
from wall import wall

def run6():
    wall.upTo(30, speed=200)#nur bei run 6 alleine
    wait_for_button_pressed()#nur bei run 6 alleine

    wall.upTo(28)
    wall.upTo(100, wait=False)
    drive.drive_to(725, 0)
    drive.rotate_to_forward(44)
    wall.upTo(40, speed=400)
    drive.drive_to(100, 44, speed=200)
    drive.straight_ms(170, speed=120)
    wait(200)
    #wait_for_button_pressed()
    drive.drive_to(-90, 43, speed=100)
    #wait_for_button_pressed()
    wall.upTo(1, speed=400)
    drive.drive_to(15, 43, speed=100)
    drive.drive_to(-75, 43, speed=100)
    drive.drive_to(10, 43, speed=100)
    #wait_for_button_pressed()
    wall.rightTo(30, 400)
    wall.upTo(50)
    wall.rightTo(60)
    wall.upTo(45)
    wall.upTo(100, 10000)
    wall.rightTo(70)
    wall.rightTo(40)
    #wait_for_button_pressed()
    drive.rotate_to_backward(0)
    drive.drive_to(10, 0)
    wall.rightTo(65, wait=False)
    drive.rotate_to_forward(-90)
    wall.upTo(40, speed=300, wait=False)
    drive.drive_to(30, -90)
    wall.upTo(18)
    drive.drive_to(-60, -90)
    wall.rightTo(0)
    drive.drive_to(65, -90)
    wall.rightTo(70, speed=300)
    wall.upTo(100)
    drive.drive_to(150, -90)
    wall.rightTo(75, wait=False)
    wall.upTo(18, speed=400, wait=False)
    drive.drive_to(205, -90, speed=200)
    wall.upTo(80)
    wait(1000)
    wall.rightTo(0, speed=400)



