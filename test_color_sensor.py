from pybricks.hubs import PrimeHub
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Axis
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub()

color_sensor = ColorSensor(Port.E)
while True:
    wait(100)
    print(color_sensor.reflection())
