from pybricks.parameters import Button
from pybricks.tools import wait
from pybricks.tools import StopWatch
from drive import drive
from hub import hub
from wall import wall

class Mode:
    LEFT_RIGHT = 1
    UP_DOWN = 2

mode = Mode.LEFT_RIGHT
watch:StopWatch=StopWatch()
while True:
    pressed = hub.buttons.pressed()
    if Button.BLUETOOTH in pressed:
        if mode == Mode.LEFT_RIGHT:
            mode = Mode.UP_DOWN
        else:
            mode = Mode.LEFT_RIGHT
    if any(pressed):
        if mode ==  Mode.LEFT_RIGHT:
            if Button.RIGHT in pressed:
                wall.right()
            elif Button.LEFT in pressed:
                wall.left()
        elif mode == Mode.UP_DOWN:
            if Button.RIGHT in pressed:
                wall.up()
            elif Button.LEFT in pressed:
                wall.down()
    else:
        wall.stop()
    # wait(1)

    if watch.time()>1000:
        watch.reset()
        print("Drive: Distance:", drive.distance(), "mm, Angle:", drive.angle(), "deg (clockwise)")
        print("Wall: up/down:", wall.up_pos(), "mm; right:", wall.right_pos())

