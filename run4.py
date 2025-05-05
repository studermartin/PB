from pybricks.tools import wait
from pybricks.parameters import Stop
from drive import drive
from hub import wait_for_button_pressed
from wall import wall

def run4():

    wall.upTo(5)#nur bei run 4 einzeln
    wall.rightTo(55)#nur bei run 4 einzeln
    wait_for_button_pressed()#nur bei run 4 einzeln

    wall.rightTo(-20, speed=100)
    wall.rightTo(20, speed=200)
    drive.drive_to(555, 0)
    wait(50)
    wall.rightTo(30, wait=False)
    wall.upTo(50, wait=False)
    drive.rotate_to_forward(-49)
    wall.upTo(47)    # Wand slll nicht verklemmen
    wall.upTo(120) 
    drive.drive_to(65, -45-4)
    wall.upTo(35)
    drive.straight_ms(200, 150)
    wall.upTo(0)
    wait(200)
    wall.upTo(102)
    drive.drive_to(-60, -50)
    wall.upTo(26, wait=False)
    drive.rotate_to_backward(1)
    wall.rightTo(62, wait=False)
    #wait_for_button_pressed()
    drive.drive_to(-610, 1, speed=450)

run4()
    