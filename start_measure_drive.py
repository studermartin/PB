from hub import wait_for_button_pressed
from drive import drive


print("Test drive distance")
print("Measure and press button. Drive distance is 700 mm.")
wait_for_button_pressed()

drive.straigt(700)

print("Measure and press button. Robot goes back.")
wait_for_button_pressed()

drive.straigt(-700)



