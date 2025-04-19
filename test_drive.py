from pybricks.tools import wait
from pybricks.tools import StopWatch
from drive import drive
from hub import hub
from hub import wait_for_button_pressed


drive.turn_to(90)
drive.turn_to(0)
drive.drive_to(600,0,straight_speed=300)
drive.drive_to(-600,0,straight_speed=300)


exit()



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

