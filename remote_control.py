from pybricks.parameters import Button
from pybricks.tools import wait
from pybricks.tools import StopWatch
from drive import drive
from hub import hub
from wall import wall


while True:
    pressed = hub.buttons.pressed()
    if Button.RIGHT in pressed:
        wall.right()
    else:
        wall.stop()
    print(wall.right_pos())
    wait(100)

while True:
    print(drive.drive_base.distance())
    wait(1000)

