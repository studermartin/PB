from pybricks.hubs import PrimeHub
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Axis

# Initialize the hub.
hub = PrimeHub()

watch = StopWatch()

def biip():
    hub.speaker.beep(500)

biip()

# Get the acceleration or angular_velocity along a single axis.
# If you need only one value, this is more memory efficient.
while True:

    heading = hub.imu.heading()

    print("Heading [Grad]: " + str(heading))
    wait(1000)
    
    time = watch.time()
    print("Zeit [ms]: " + str(time))

    