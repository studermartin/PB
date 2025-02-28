from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

drive_base.use_gyro(True)

# Drive forward by 500mm (half a meter).
drive_base.straight(500)

# Turn around clockwise by 180 degrees.
drive_base.turn(180)

# Drive forward again to get back to the start.
drive_base.straight(500)

# Turn around counterclockwise.
drive_base.turn(-180)

# Schaune mer mal