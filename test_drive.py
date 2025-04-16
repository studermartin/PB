from pybricks.tools import wait
from drive import drive
from hub import hub
from hub import wait_for_button_pressed

def test_reset():
    drive.reset()
    
    assert -2<drive.angle()<2

    # turn to 45 degree
    drive.turn_to(45)
    wait(100)
    assert 42<drive.angle()<48

    # 45 degree clockwise
    drive.turn_to(45)
    assert 42<drive.angle()<48, "Should not move because the last turn_to already set to 45 degree."

    drive.reset()
    assert -2<drive.angle()<2

    # 45 degree clockwise
    drive.turn_to(45)
    assert 42<drive.angle()<48, "Should not move because the last turn_to already set to 45 degree."

test_reset()
   


drive.straigt(700)



# wait(2000)
print(-hub.imu.heading())
# drive.straight(100)
drive.turn(20)
wait(500)
print(-hub.imu.heading())
drive.turn(20)
wait(500)
print(-hub.imu.heading())
drive.turn(20)
wait(500)
print(-hub.imu.heading())
drive.turn(20)
wait(500)
print(-hub.imu.heading())
drive.turn(20)


drive.stop()
# drive.straigt(750)
# drive.turn(90)
# wait(100)
# drive.straigt(600)
# drive.turn(180)
# drive.straigt(600)
# drive.turn(-90)


# drive.straigt(749)
# drive.turn(-90)
# drive.straigt(-100)

# drive.rotate_forward(90)
# wait(2000)
# drive.rotate_forward(-90)
# wait(2000)
# run_task(drehe_auf(90, True, Raeder.RECHTS))
# wait(2000)
# run_task(drehe_auf(-90, True, Raeder.RECHTS))
# wait(2000)
# run_task(drehe_auf(90, True, Raeder.LINKS))
# wait(2000)
# run_task(drehe_auf(-90, True, Raeder.LINKS))

# wait(2000)
# run_task(drehe_auf(45, True, Raeder.LINKS))
# wait(2000)
# run_task(drehe_auf(-45, True, Raeder.LINKS))


# run_task(gyro_fahren(10, 500))

# run_task(gyro_fahren_timeout(10, 500))

# run_task(drehe_auf(90, True))
# wait(2000)
# run_task(drehe_auf(90, False))



wait(10000)

