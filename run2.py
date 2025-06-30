from pybricks.tools import wait
from pybricks.parameters import Stop
from drive import drive
from hub import wait_for_button_pressed
from wall import wall

def run2():


    wall.rightTo(-20)
    wait(100)
    wall.rightTo(7)
    drive.straight_ms(500, -300)
    wait(50)
    wall.upTo(45, speed=400, wait=False)
    drive.drive_to(307, 0)
    wall.rightTo(-47, wait=False)
    drive.arc(-440, angle=90)

    # Anglerfisch
    wall.upTo(5, speed=400, wait=False)
    drive.drive_to(280, -90)
    drive.drive_to(-10, -90)

    # Meeresbodenprobe
    wall.rightTo(65, speed=300)
    drive.drive_to(113, -90)
    wall.rightTo(20, wait=False)
    wall.upTo(0, wait=False)
    drive.drive_to(230, -90)

    # Wasserprobe wegschieben 
    wall.rightTo(-65, speed=200, wait=False)
    drive.drive_to(60, -90, speed=200)
    wall.rightTo(-50, speed=250, wait=False)
    drive.drive_to(80, -90, speed=300)

    #Krill einsammeln
    wall.upTo(5, wait=False)
    wall.rightTo(35, speed=400)#40
    drive.drive_to(150, -90)
    #wait(30)
    #wall.upTo(10, speed=75, wait=False)
    drive.straight_ms(300, speed=150)

    # Taucher einsammeln, Haifisch freilassen, Korallenknospen aufstellen
    wall.upTo(35)
    drive.drive_to(-10, -90, speed=150)
    wall.upTo(0)

    # Zurückfahren
    drive.drive_to(-140, -90)
    wall.rightTo(55, speed=400, wait=False)
    drive.rotate_to_backward(-158)
    drive.drive_to(80, -158, speed=100)
    wall.rightTo(0, wait=False)
    drive.drive_to(610, -158)
    drive.stop()