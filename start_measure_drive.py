from hub import wait_for_button_pressed
from drive import drive


print("Test drive distance")
print("Measure and press button. Drive distance is 300 mm.")
wait_for_button_pressed()

drive.straigt(300)

print("Measure and press button. Robot goes back.")
wait_for_button_pressed()

drive.straigt(-300)



