from pybricks.tools import wait
from drive import drive
from hub import hub

def test_turn_to():
    drive.reset()

    # turn to 45 degree
    drive.turn_to(45)
    assert 42<drive.angle()<48

    drive.turn_to(0)
    current_angle = drive.angle()
    assert -3<current_angle<3, f"Expected angle: {0} deg, current angle:{current_angle} deg"


def test_reset():
    drive.reset()
    
    assert -2<drive.angle()<2

    # turn to 45 degree
    drive.turn_to(45)
    wait(100)
    assert 42<drive.angle()<48

    # 45 degree clockwise
    drive.turn_to(45)
    assert 42<drive.angle()<48, "Should not move because the last turn_to already set to 45 degree."

    drive.reset()
    assert -2<drive.angle()<2

    # 45 degree clockwise
    drive.turn_to(45)
    assert 42<drive.angle()<48, "Should not move because the last turn_to already set to 45 degree."

    drive.turn_to(-45)

def test_drive_to_straight():
    drive.reset()
    
    distance = 200
    start_distance = drive.drive_base.distance()
    target_distance = start_distance + distance

    drive.drive_to(distance, 0)
    wait(500)

    # print("Distance: ", drive.drive_base.distance())
    current_distance = drive.drive_base.distance()
    assert target_distance-5 <= current_distance <= target_distance+5, f"Expected distance: {distance} mm, current distance: {current_distance} mm"

    drive.drive_to(-distance, 0)
    current_distance = drive.drive_base.distance()
    assert 0-5 <= current_distance <= 0+5, f"Expected distance: {distance} mm, current distance: {current_distance} mm"

def test_rotate_backward_to(expected_angle:float):
    drive.reset()

    drive.rotate_to_backward(expected_angle)
    wait(200)

    current_angle = drive.angle()
    assert expected_angle-4 <= current_angle <= expected_angle+4, f"Expected angle: {expected_angle} deg, current angle: {current_angle} deg"
    assert drive.drive_base.distance() < 0, f"Expected backward drive (distance < 0): distance: {drive.drive_base.distance()} mm"

def test_rotate_backward_to_both_directions():
    test_rotate_backward_to(45)
    test_rotate_backward_to(-45)


def test_rotate_forward_to(expected_angle:float):
    drive.reset()

    drive.rotate_to_forward(expected_angle)
    wait(500)

    current_angle = drive.angle()
    assert expected_angle-4 <= current_angle <= expected_angle+4, f"Expected angle: {expected_angle} deg, current angle: {current_angle} deg"
    assert drive.drive_base.distance() > 0, f"Expected forward drive (distance > 0): distance: {drive.drive_base.distance()} mm"
    
def test_rotate_forward_to_both_directions():
    test_rotate_forward_to(45)
    test_rotate_forward_to(-45)

test_rotate_forward_to_both_directions()
test_rotate_backward_to_both_directions()
test_turn_to()
test_reset()
test_drive_to_straight()

   

