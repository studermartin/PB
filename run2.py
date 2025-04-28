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
    wall.upTo(5)
    drive.drive_to(307, 0)
    wall.rightTo(-35, wait=False)
    drive.drive_base.arc(-440, angle=90)

    # Anglerfisch
    drive.drive_to(273, -90)

    # Meeresbodenprobe
    wall.rightTo(65, speed=300)
    drive.drive_to(120, -90)
    wall.rightTo(20, wait=False)
    wall.upTo(0, wait=False)
    drive.drive_to(180, -90)

    # Wasserprobe wegschieben 
    wall.rightTo(-50, speed=200, wait=False)
    drive.drive_to(100, -90)
    wall.rightTo(-25, speed=250, wait=False)
    wall.upTo(30)
    drive.drive_to(45, -90, speed=300)

    #Krill einsammeln
    wall.upTo(5)
    wall.rightTo(55, speed=400, wait=False)
    drive.drive_to(215, -90, speed=350)
    #wall.rightTo(55, speed=300)

    wait_for_button_pressed()



    # Anglerfisch 
    drive.drive_to(645, -89)
    wall.rightTo(-20)

    # Bodenprobe aufnehmen
    drive.drive_to(-43, -90)
    wall.rightTo(75)
    drive.drive_to(170, -90)
    
    # wait_for_button_pressed()

    # Wasserprobe wegschieben 
    wall.rightTo(30)
    drive.drive_to(190, -90)####

    wall.rightTo(-55, wait=False)

    drive.drive_to(90, -90)

    wall.rightTo(-75)
    wall.rightTo(-55, wait=False)
    wall.upTo(30)

    # await gyro_fahren(3.8, 400, 90)
    drive.drive_to(38, -90)
    
    wall.rightTo(-45)
    wall.upTo(5)
    wall.rightTo(-10)
    wall.rightTo(10)
    wall.rightTo(45, wait=False)

    # await gyro_fahren(17, 1050, 88)#
    drive.drive_to(170,-88)
    
    wait(100)

    # await fahre_sekunden(0.4, 500)
    drive.straight_ms(400,200)

    wall.upTo(35)
    wall.rightTo(55)
    wall.upTo(10)
    
    # await gyro_fahren(-20, 1050, 90)
    drive.drive_to(-200,-90)

    wall.upTo(0, wait=False)
    wall.rightTo(0, wait=False)

    # await drehe_auf(140, Drehrichtung.GEGENUHRZEIGERSINN, Raeder.LINKS)
    drive.rotate_to_backward(-140)

    wall.rightTo(30)

    # await gyro_fahren(13, 1050, 140)
    drive.drive_to(130,-140)
    
    wall.rightTo(0)

    # await gyro_fahren(57, 1050, 140)
    drive.drive_to(570,-140)


run2()

