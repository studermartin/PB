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
    drive.drive_to(-110, 0)
    wall.upTo(110)
    drive.drive_to(-250, 0, speed=450)
    wall.rightTo(0, wait=False)
    drive.rotate_to_forward(-14)
    drive.drive_to(420, -14)
    drive.rotate_to_forward(15)
    drive.drive_to(750, 15)
    wall.upTo(10)
    wait_for_button_pressed()

    
run5()