from pybricks.tools import wait
from pybricks.parameters import Axis, Stop
from drive import drive
from hub import wait_for_button_pressed
from hub import beepLow, hub

hub.imu.settings(angular_velocity_threshold=10, acceleration_threshold=1000)
drive.turn_to(0, then=Stop.HOLD)
drive.stop()
while True:
    if not hub.imu.ready():
        print("Ready", hub.imu.ready())
    print(drive.angle())
    # print("Stationary:", hub.imu.stationary())
    # print("imu.acceleration:", hub.imu.acceleration(Axis.Z, calibrated=True), "angular_velocity:", hub.imu.angular_velocity(None, calibrated=True))
    wait(1000) 


wait_for_button_pressed()
drive.turn_to(0)
while True:
    print(drive.angle())
    print(not hub.imu.ready())
    wait(1000)
wait_for_button_pressed()


# wait_for_button_pressed()
# drive.straight(100)
# wait_for_button_pressed()
# drive.straight(100, straight_acceleration=9000)
# drive, drive_to, straight_ms, straight

#drive.turn_to(90)
#drive.turn_to(0)
#drive.drive_to(600,3,speed=300)
#drive.drive_to(-600,3,speed=300)

# print(drive.get_acceleration_deceleration())
# drive.set_acceleration_deceleration(800, 800)
# print(drive.get_acceleration_deceleration())
# drive.set_acceleration_deceleration(800, 800)

# drive.drive_to(200, 0, speed=160)



"""
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

"""