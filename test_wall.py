import umath
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub

from wall import *
from hub import *

hub = PrimeHub()

def print_color():
    while True:
        print(wall.center_reflection())
        print(wall.center_color())
        wait(100)

wall.center()
exit()

# Check direction
print("Wall goes 20 mm to the right...", None)
wall.right(20)
print("done.")
wait(1000)

print("Wall goes 20 mm up...", None)
wall.up(20)
print("done.")
wait(1000)

# check initial position
print("Wall goes down...", None)
wall.downToStop()
print("done.")
wait(1000)
print("Wall is centered...", None)
wall.center()
print("done.")
wait(2000)
wall.reset_pos()


# Up/Down
wait(1000)
wall.upTo(20)
hub.speaker.beep(500)
wall.upTo(20)
# hub.speaker.beep(500)
wall.upTo(40)
# hub.speaker.beep(500)
# wall.upTo(40)
# wall.upTo(10)
# wall.upTo(10)
# wall.left(40)

# deprecated up/down
# wait(1000)
# wand_initialisieren()
# ausführen_wand_vertikal(0)
# hub.speaker.beep(500)
# ausführen_wand_vertikal(2)

# Left/right



wait(1000)
# # wait(2000)
# wall.left(20)
# # print("1")

wall.leftTo(40)
# print("2")
# wait_for_button_pressed()

# print("3")
# wall.leftTo(20)
# print("4")
# hub.speaker.beep(500)
# wall.upTo(20)
# hub.speaker.beep(500)
# wall.upTo(40)
# hub.speaker.beep(500)
# wall.upTo(40)
# wall.upTo(10)
# wall.upTo(10)
# wall.left(40)
