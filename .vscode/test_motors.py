from pybricks.hubs import PrimeHub
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Axis, Direction
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.iodevices import PUPDevice
from uerrno import ENODEV

RUN_TIME=2000
RUN_SPEED = 500

hub = PrimeHub()

def run_motor(port: Port, direction: Direction):
        motor = Motor(port, direction)
        motor.run_time(RUN_TIME, RUN_SPEED)
        motor.close()

ports = [ Port.A, Port.B, Port.C, Port.D, Port.E, Port.F]
print(ports)

print("Run all motors on all ports with for", RUN_TIME, "ms with speed", RUN_SPEED, " in both directions.")
print("Port.C: Expected")
print("  CLOCKWISE: wall to the right")
print("Port.D: Expected")
print("  CLOCKWISE: wall down")
print("  COUNTERCLOCKWISE: wall up")

for port in ports:
    print(port)
    for direction in [Direction.CLOCKWISE, Direction.COUNTERCLOCKWISE]:
        try:
            run_motor(port, direction)
            print("  ", direction)
            wait(RUN_TIME)
        except OSError as ex:
            if ex.args[0] == ENODEV:
                # No motor on this port
                print(port, ": no motor")
                break
            else:
                raise





