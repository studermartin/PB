from pybricks.hubs import PrimeHub
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Axis
from pybricks.pupdevices import Motor
from pybricks.parameters import Port

# Initialize the hub.
hub = PrimeHub()

motor = Motor(Port.C)
motor.run_time(100, 2000)

