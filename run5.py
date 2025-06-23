from pybricks.tools import wait
from drive import drive
from hub import wait_for_button_pressed
from wall import wall

def run5():
    #wall.upTo(40)#nur bei run 5 einzeln
    #wall.rightTo(60)#nur bei run 5 einzeln
    #wait_for_button_pressed()#nur bei run 5 einzeln


    drive.drive_to(943, 0)
    drive.drive_to(-150, 0, straight_acceleration=100)
    wall.upTo(110)
    drive.drive_to(-230, 0, speed=350,)
    #wait_for_button_pressed()
    #wall.rightTo(0, wait=False)
    drive.rotate_to_forward(-14)
    drive.drive_to(325, -14)
    wall.upTo(65)
    drive.drive_to(-120, -14)
    drive.drive_to(220, -14)
    drive.rotate_to_forward(15)
    wall.upTo(80, wait=False)
    wall.rightTo(0, wait=False)
    wall.upTo(40, wait=False)
    drive.drive_to(750, 15, speed=500)
    
    drive.stop()

    