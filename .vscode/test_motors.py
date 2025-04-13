from pybricks.hubs import PrimeHub
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Axis, Direction
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.iodevices import PUPDevice

hub = PrimeHub()

MOTOR_PIDS:dict[str,tuple[int,int,int,int]] = { "big":(42484, 21242, 5310, 8, 15),
             "middle": (15117, 7558, 1889, 8, 15)}

def find_key(input_dict, value):
    for key, val in input_dict.items():
        if val == value: return key
    return "None"

def motor_from_pid(motor: Motor):
    return find_key(MOTOR_PIDS, motor.control.pid())
    
    

def detect(port: Port):
    motor = Motor(port)
    print(motor_from_pid(motor))
    motor.close()


def test(port: Port, direction: Direction):
    motor = Motor(port, direction)
    motor.run_time(300, 1000)
    print(motor.control.pid())
    motor.close()

test(Port.D, Direction.CLOCKWISE) 



ports = [ Port.A, Port.B, Port.C, Port.D, Port.E, Port.F]
print(ports)


for port in ports:
    # for direction in [Direction.CLOCKWISE, Direction.COUNTERCLOCKWISE]:
        print("Port ", port)
        # try:
        #     pass
        # catch():
        #     pass
        # test(port, direction)

        # detect(port)

        pupDevice:PUPDevice=PUPDevice(port)
        print(pupDevice.info())




