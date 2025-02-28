from pybricks.hubs import PrimeHub
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Axis
from pybricks.pupdevices import Motor
from pybricks.parameters import Port

# Initialize the hub.
hub = PrimeHub()

motor_A = Motor(Port.B)
motor_A.run_time(100, 5000)

