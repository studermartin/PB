from pybricks import version
from pybricks.iodevices import PUPDevice
from pybricks.parameters import Port
from uerrno import ENODEV
from hub import hub

# Source: https://docs.pybricks.com/en/latest/iodevices/pupdevice.html

print(version)
print(hub.system.info())
print(hub.battery.voltage(), "mV")
assert hub.battery.voltage()>8000,  "Battery voltage below 8000."

# Dictionary of device identifiers along with their name.
DEVICE_NAMES:dict[int,str] = {
    # pybricks.pupdevices.DCMotor
    1: "Wedo 2.0 Medium Motor",
    2: "Powered Up Train Motor",
    # pybricks.pupdevices.Light
    8: "Powered Up Light",
    # pybricks.pupdevices.Motor
    38: "BOOST Interactive Motor",
    46: "Technic Large Motor",
    47: "Technic Extra Large Motor",
    48: "SPIKE Medium Angular Motor",
    49: "SPIKE Large Angular Motor",
    65: "SPIKE Small Angular Motor",
    75: "Technic Medium Angular Motor",
    76: "Technic Large Angular Motor",
    # pybricks.pupdevices.TiltSensor
    34: "Wedo 2.0 Tilt Sensor",
    # pybricks.pupdevices.InfraredSensor
    35: "Wedo 2.0 Infrared Motion Sensor",
    # pybricks.pupdevices.ColorDistanceSensor
    37: "BOOST Color Distance Sensor",
    # pybricks.pupdevices.ColorSensor
    61: "SPIKE Color Sensor",
    # pybricks.pupdevices.UltrasonicSensor
    62: "SPIKE Ultrasonic Sensor",
    # pybricks.pupdevices.ForceSensor
    63: "SPIKE Force Sensor",
    # pybricks.pupdevices.ColorLightMatrix
    64: "SPIKE 3x3 Color Light Matrix",
}

def find_key(input_dict, value):
    for key, val in input_dict.items():
        if val == value: 
            return key
    return "None"

EXPECTED_DEVICE_CONFIG:dict[int,str]={}
EXPECTED_DEVICE_CONFIG[Port.A]=find_key(DEVICE_NAMES,"SPIKE Large Angular Motor")
EXPECTED_DEVICE_CONFIG[Port.B]=find_key(DEVICE_NAMES,"SPIKE Large Angular Motor")
EXPECTED_DEVICE_CONFIG[Port.C]=find_key(DEVICE_NAMES,"SPIKE Medium Angular Motor")
EXPECTED_DEVICE_CONFIG[Port.D]=find_key(DEVICE_NAMES,"SPIKE Large Angular Motor")
EXPECTED_DEVICE_CONFIG[Port.E]=find_key(DEVICE_NAMES,"SPIKE Color Sensor")
EXPECTED_DEVICE_CONFIG[Port.F]=find_key(DEVICE_NAMES,"SPIKE Force Sensor")


# Make a list of known ports.
ports = [Port.A, Port.B]

# On hubs that support it, add more ports.
try:
    ports.append(Port.C)
    ports.append(Port.D)
except AttributeError:
    pass

# On hubs that support it, add more ports.
try:
    ports.append(Port.E)
    ports.append(Port.F)
except AttributeError:
    pass

# Go through all available ports.
for port in ports:

    # Try to get the device, if it is attached.
    try:
        device = PUPDevice(port)
    except OSError as ex:
        if ex.args[0] == ENODEV:
            # No device found on this port.
            print(port, ": ---")
            continue
        else:
            raise

    # Get the device id and the expected device id
    id = device.info()["id"]
    expected_id=EXPECTED_DEVICE_CONFIG[port]

    # Look up the name.
    try:
        print(port, ":", DEVICE_NAMES[id])
        if id != expected_id:
            print(" Expected configuration: ", DEVICE_NAMES[expected_id])
    except KeyError:
        print(port, ":", "Unknown device with ID", id)