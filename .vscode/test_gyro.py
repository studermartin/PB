from pybricks.hubs import PrimeHub
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Axis
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop

# Initialize the hub.
hub = PrimeHub()

watch = StopWatch()

def biip():
    hub.speaker.beep(500)

biip()

print("Ready", hub.imu.ready())

# Get the acceleration or angular_velocity along a single axis.
# If you need only one value, this is more memory efficient.
for i in range(10):

    heading = hub.imu.heading()

    print("Heading [Grad]: " + str(heading))
    wait(1000)
    
    time = watch.time()
    print("Zeit [ms]: " + str(time))

# motor_A = Motor(Port.A)
# motor_A.run_time(100, 5000)

for i in range(40):

    heading = hub.imu.heading()

    print("Heading [Grad]: " + str(heading))
    wait(1000)
    
    time = watch.time()
    print("Zeit [ms]: " + str(time))
