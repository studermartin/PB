from pybricks.tools import wait
from pybricks.parameters import Stop
from drive import drive
from hub import wait_for_button_pressed,  hub, force_sensor, beepHigh
from wall import wall
from run1 import run1
from run2 import run2
from run3 import run3
from run4 import run4
from run5 import run5
from run6 import run6

run_to_start = 1
hub.display.number(run_to_start)

pressed = []
while not force_sensor.pressed():
    pressed = hub.buttons.pressed()
    if  any(pressed):
        run_to_start = run_to_start+1
        if run_to_start > 6:
            run_to_start = 1
        hub.display.number(run_to_start)
    wait(100)
beepHigh()

if run_to_start <1:
    print("Run 1")
    run1()
    wait_for_button_pressed()
    drive.reset()

if run_to_start<2:
    print("Run 2")
    run2()
    wait_for_button_pressed()
    drive.reset()

if run_to_start<3:
    print("Run 3")
    run3()
    wait_for_button_pressed()
    drive.reset()

if run_to_start<4:
    print("Run 4")  
    run4()
    wait_for_button_pressed()
    drive.reset()

if run_to_start<5:
    print("Run 5")
    run5()
    wait_for_button_pressed()
    drive.reset()

if run_to_start<6:
    run6()
