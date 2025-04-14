from wall import wall
from hub import wait_for_button_pressed

print("Wall down and center", None)
wall.downToStop()
wall.center()
print("done.")
wall.reset_pos()

print("Horizontal movement: ")
print("Measure edge of wall and press button.")
wait_for_button_pressed()

print("Wall goes 70 mm to the left...", end=' ')
wall.leftTo(70)
print("done.")

# 
print("Vertical movement: ")
print("Measure upper level of wall and press button.")
wait_for_button_pressed()

print("Wall goes up to 100 mm...", end=' ')
wall.upTo(100)
print("done.")

wait_for_button_pressed()
wall.upTo(0)




