from pybricks.tools import wait

from wall import wall
from hub import hub


wall.rightTo(15)
wall.upTo(50)
wall.rightTo(35)
wall.rightTo(50, wait=False)
wall.upTo(72)

exit()

def print_color():
    while True:
        print(wall.center_reflection())
        print(wall.center_color())
        wait(100)

# Check direction
print("Wall goes 50 mm to the right...", end="")
wall.right(50)
print("done.")
wait(1000)

print("Wall goes 50 mm to the left with 100 mm/s...", end="")
wall.left(50, 100)
print("done.")
wait(1000)

print("Wall goes 50 mm up...", end="")
wall.up(50)
print("done.")
wait(1000)

print("Wall goes 50 mm down...", end="")
wall.down(50, 80)
print("done.")
wait(1000)


# check initial position
print("Wall goes down...", None)
wall.downToStop()
print("done.")
wait(1000)
print("Wall is centered...", None)
wall.center()
print("done.")
wait(2000)
wall.reset_pos()


# Up/Down
wait(1000)
wall.upTo(20)
hub.speaker.beep(500)
wall.upTo(20)
# hub.speaker.beep(500)
wall.upTo(40)
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



wait(1000)
# # wait(2000)
# wall.left(20)
# # print("1")

wall.leftTo(40)
# print("2")
# wait_for_button_pressed()

# print("3")
# wall.leftTo(20)
# print("4")
# hub.speaker.beep(500)
# wall.upTo(20)
# hub.speaker.beep(500)
# wall.upTo(40)
# hub.speaker.beep(500)
# wall.upTo(40)
# wall.upTo(10)
# wall.upTo(10)
# wall.left(40)
