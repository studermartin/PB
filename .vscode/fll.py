from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase



left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

drive_base.use_gyro(True)

hub.speaker.beep(500)


##########################################################
### Signaltöne
##########################################################

def beepLow():
    hub.speaker.beep(440, 100)

def beepHigh():
    hub.speaker.beep(880, 100)


##########################################################
### Wand
##########################################################
