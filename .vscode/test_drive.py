from pybricks.tools import wait
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import *
from pybricks import version
from drive import *

# drive.straigt(100)
# drive.turn(90)
# drive.turn(-90)
# drive.straigt(-100)

wait(2000)

# run_task(gyro_fahren(10, 500))

run_task(gyro_fahren_timeout(10, 500))

wait(10000)

