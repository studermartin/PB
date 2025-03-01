from pybricks.tools import wait
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks import version
from drive import *

print(version)


print(hub.imu.settings())
hub.imu.settings(angular_velocity_threshold=1, acceleration_threshold=1000)
# hub.imu.settings(heading_correction=361)
print(hub.imu.settings())


print("Ready", hub.imu.ready())
print()

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A, Direction.CLOCKWISE)

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

drive_base.use_gyro(True)
drive_base.settings(turn_rate=50)

wait(2000)

# Drive forward by 500mm (half a meter).
drive_base.straight(500, then=Stop.HOLD, wait=False)
while not drive_base.stalled():
    wait(500)
drive_base.stop()

hub.speaker.beep(200)
for i in range(2):
    heading = hub.imu.heading()

    print("Heading [Grad]: " + str(heading))
    wait(1000)


wait(1000)


# Turn around clockwise by 180 degrees.

drive_base.turn(180, wait=True, then=Stop.HOLD)
hub.speaker.beep(500)

drive_base.use_gyro(False)
wait(500)
drive_base.use_gyro(True)

# drive_base.reset()

# Drive forward again to get back to the start.
drive_base.straight(100, then=Stop.HOLD)
for n in range(2):

    heading = hub.imu.heading()

    print("Heading [Grad]: " + str(heading))
    print("Ready", hub.imu.ready())

    
    wait(1000)


wait(1000)

# Turn around counterclockwise.
wait(500)

drive_base.turn(-180, then=Stop.HOLD)



heading = hub.imu.heading()
print("Heading [Grad]: " + str(heading))



for n in range(100):

    heading = hub.imu.heading()

    print("Heading [Grad]: " + str(heading))
    print("Ready", hub.imu.ready())

    wait(1000)


