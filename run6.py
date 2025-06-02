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
    wall.upTo(40, speed=400, wait=False)
    drive.drive_to(100, 44, speed=200)
    drive.straight_ms(500)
    wait(200)
    #wait_for_button_pressed()
    drive.drive_to(-60, 43, speed=100)
    #wait_for_button_pressed()
    wall.upTo(0, speed=400)
    #drive.drive_to(-35, 43, speed=100)
    drive.drive_to(-53, 43, speed=100)
    wait_for_button_pressed()
    wall.rightTo(30, 400)
    wall.upTo(50)
    wall.rightTo(60)
    wall.upTo(105)
    wall.rightTo(40)
    #wait_for_button_pressed()
    drive.rotate_to_backward(0)
    drive.drive_to(10, 0)
    wall.rightTo(70, wait=False)
    drive.rotate_to_forward(-90)
    wall.upTo(40, speed=300, wait=False)
    drive.drive_to(30, -90)
    wall.upTo(18)
    drive.drive_to(-30, -90)
    wall.rightTo(10)
    wait_for_button_pressed()






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
    drive.stop()