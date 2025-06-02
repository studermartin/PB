from pybricks.tools import wait
from drive import drive
from hub import wait_for_button_pressed
from wall import wall

def run5():
    wall.upTo(40)#nur bei run 5 einzeln
    wall.rightTo(62)#nur bei run 5 einzeln
    wait_for_button_pressed()#nur bei run 5 einzeln


    drive.straight(960,straight_acceleration=(30))
    wait_for_button_pressed()
    drive.straight(-160,straight_acceleration=100)
    #wait_for_button_pressed()
    wall.upTo(90)
    #wait_for_button_pressed()
    drive.drive_to(-260, straight_acceleration=(9775))
    #wait_for_button_pressed()
    #wall.rightTo(0, wait=False)
    drive.rotate_to_forward(-14)
    drive.drive_to(425, -14)
    drive.rotate_to_forward(15)
    drive.drive_to(750, 15)
    wall.upTo(30)
    drive.stop()

    