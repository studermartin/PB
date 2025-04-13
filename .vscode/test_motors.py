from pybricks.hubs import PrimeHub
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Axis, Direction
from pybricks.pupdevices import Motor
from pybricks.parameters import Port

# Initialize the hub.
hub = PrimeHub()

motor = Motor(Port.D, Direction.CLOCKWISE)
motor.run(10)

wait(2000)