from pybricks.tools import wait
from drive import drive
from wall import wall
from hub import wait_for_button_pressed

def run2():

    wall.rightTo(-20)
    wait(100)

    wall.rightTo(7)
    
    drive.straigt_ms(5, -300)
    

    wait(50)
    wait_for_button_pressed()
    
    # await gyro_fahren(66.5, 900, 0)
    drive.turn_to_and_drive(0, 665)
    wall.rightTo(-20, wait=False)

    # await drehe_auf(89, Drehrichtung.GEGENUHRZEIGERSINN, Raeder.RECHTS)
    drive.rotate_forward(-89)
    
    wall.rightTo(-35)

    # await gyro_fahren(63.5, 1050, 89)
    drive.turn_to_and_drive(-89, 635)

    wall.rightTo(-20)

    # await gyro_fahren(-4.3, 500, 90)
    drive.turn_to_and_drive(-90, -43)
    
    wall.rightTo(75)

    # await gyro_fahren(15, 900, 90)
    drive.turn_to_and_drive(-90,150)

    wall.rightTo(30)
    
    # await gyro_fahren(18, 1050, 90)
    drive.turn_to_and_drive(-90,180)
    
    wall.rightTo(-55, wait=False)

    # await gyro_fahren(10, 500, 90)
    drive.turn_to_and_drive(-90,100)
    
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
    drive.turn_and_drive(-88,170)
    
    wait(100)

    # await fahre_sekunden(0.4, 500)
    drive.straigt_ms(4,500)

    wall.upTo(35)
    wall.rightTo(55)
    wall.upTo(10)
    
    # await gyro_fahren(-20, 1050, 90)
    drive.turn_and_drive(-90,-200)

    wall.upTo(0, wait=False)
    wall.rightTo(0, wait=False)

    # await drehe_auf(140, Drehrichtung.GEGENUHRZEIGERSINN, Raeder.LINKS)
    drive.rotate_to_backward(-140)

    wall.rightTo(30)

    # await gyro_fahren(13, 1050, 140)
    drive.turn_to_and_drive(-140,130)
    
    wall.rightTo(0)

    # await gyro_fahren(57, 1050, 140)
    drive.turn_to_and_drive(-140,57)




