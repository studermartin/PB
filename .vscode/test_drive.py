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

# drive.rotate_forward(90)
# wait(2000)
# drive.rotate_forward(-90)
# wait(2000)
# run_task(drehe_auf(90, True, Raeder.RECHTS))
# wait(2000)
# run_task(drehe_auf(-90, True, Raeder.RECHTS))
# wait(2000)
# run_task(drehe_auf(90, True, Raeder.LINKS))
# wait(2000)
# run_task(drehe_auf(-90, True, Raeder.LINKS))

wait(2000)
run_task(drehe_auf(45, True, Raeder.LINKS))
wait(2000)
run_task(drehe_auf(-45, True, Raeder.LINKS))


# run_task(gyro_fahren(10, 500))

# run_task(gyro_fahren_timeout(10, 500))

# run_task(drehe_auf(90, True))
# wait(2000)
# run_task(drehe_auf(90, False))



wait(10000)

