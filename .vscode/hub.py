from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis
from pybricks.tools import wait, StopWatch

hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)

def wait_for_button_pressed():
    pressed = []
    while not any(pressed):
        pressed = hub.buttons.pressed()
        wait(10)
