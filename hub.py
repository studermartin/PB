from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ForceSensor
from pybricks.parameters import Axis, Port
from pybricks.tools import wait

hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)

_force_sensor = ForceSensor(Port.F)

def wait_for_button_pressed():
    pressed = []
    while not any(pressed) and not _force_sensor.pressed():
        pressed = hub.buttons.pressed()
        wait(100)
    beepHigh()

def beepLow():
    hub.speaker.beep(440, 100)

def beepHigh():
    hub.speaker.beep(880, 100)
