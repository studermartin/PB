from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub()

color_sensor = ColorSensor(Port.E)
while True:
    wait(100)
    print(color_sensor.reflection())
