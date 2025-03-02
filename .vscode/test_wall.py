import umath
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub

from wall import *
from hub import *

hub = PrimeHub()

# Up/Down
# wait(1000)
# wall.upTo(20, wait=False)
# hub.speaker.beep(500)
# wall.upTo(20)
# hub.speaker.beep(500)
# wall.upTo(40)
# hub.speaker.beep(500)
# wall.upTo(40)
# wall.upTo(10)
# wall.upTo(10)
# wall.left(40)

# deprecated up/down
# wait(1000)
# wand_initialisieren()
# ausführen_wand_vertikal(0)
# hub.speaker.beep(500)
# ausführen_wand_vertikal(2)

# Left/right
# wait(1000)
wall.left(80)
wall.leftTo(80)
wait_for_button_pressed()
wall.rightTo(0)
# wall.leftTo(20)
# hub.speaker.beep(500)
# wall.upTo(20)
# hub.speaker.beep(500)
# wall.upTo(40)
# hub.speaker.beep(500)
# wall.upTo(40)
# wall.upTo(10)
# wall.upTo(10)
# wall.left(40)
