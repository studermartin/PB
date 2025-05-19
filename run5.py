from pybricks.tools import wait
from drive import drive
from hub import wait_for_button_pressed
from wall import wall

def run5():
    wall.upTo(26)#nur bei run 5 einzeln
    wall.rightTo(62)#nur bei run 5 einzeln
    wait_for_button_pressed()#nur bei run 5 einzeln

    drive.drive_to(940,0)
    wait(100)
    #wait_for_button_pressed()
    drive.drive_to(-140, 0)
    #wait_for_button_pressed()
    wall.upTo(90)
    #wait_for_button_pressed()
    drive.drive_to(-260, 0, speed=500, straight_acceleration=9700)
    wall.rightTo(0, wait=False)
    drive.rotate_to_forward(-14)
    drive.drive_to(425, -14)
    drive.rotate_to_forward(15)
    drive.drive_to(750, 15)
    wall.upTo(30)
    drive.stop()

    