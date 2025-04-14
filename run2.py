from pybricks.tools import wait
from drive import drive
from wall import wall

def run2():

    wall.rightTo(-20)
    wait(100)
    wall.rightTo(7)
    drive.straigt_ms(5, -300)
    wait(50)
    wall.upTo(5)
    drive.turn_to_and_drive(0, 665)
    wall.rightTo(-20, wait=False)
    drive.rotate_forward(-89)
    wall.rightTo(-35)

    # Anglerfisch 
    drive.turn_to_and_drive(-89, 645)
    wall.rightTo(-20)

    # Bodenprobe aufnehmen
    drive.turn_to_and_drive(-90, -43)
    wall.rightTo(75)
    drive.turn_to_and_drive(-90, 170)
    
    # wait_for_button_pressed()

    # Wasserprobe wegschieben 
    wall.rightTo(30)
    drive.turn_to_and_drive(-90, 190)####

    wall.rightTo(-55, wait=False)

    drive.turn_to_and_drive(-90, 90)

    wall.rightTo(-75)
    wall.rightTo(-55, wait=False)
    wall.upTo(30)

    # await gyro_fahren(3.8, 400, 90)
    drive.turn_to_and_drive(-90, 38)
    
    wall.rightTo(-45)
    wall.upTo(0)
    wall.rightTo(-10)
    wall.rightTo(40, wait=False)

    # await gyro_fahren(17, 1050, 88)#
    drive.turn_to_and_drive(-88,170)
    
    wait(100)

    # await fahre_sekunden(0.4, 500)
    drive.straigt_ms(4,500)

    wall.upTo(35)
    wall.rightTo(55)
    wall.upTo(10)
    
    # await gyro_fahren(-20, 1050, 90)
    drive.turn_to_and_drive(-90,-200)

    wall.upTo(0, wait=False)
    wall.rightTo(0, wait=False)

    # await drehe_auf(140, Drehrichtung.GEGENUHRZEIGERSINN, Raeder.LINKS)
    drive.rotate_to_backward(-140)

    wall.rightTo(30)

    # await gyro_fahren(13, 1050, 140)
    drive.turn_to_and_drive(-140,130)
    
    wall.rightTo(0)

    # await gyro_fahren(57, 1050, 140)
    drive.turn_to_and_drive(-140,570)




