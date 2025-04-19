from pybricks.tools import wait
from pybricks.tools import StopWatch
from drive import drive
from hub import hub
from hub import wait_for_button_pressed

def test_turn_to():
    drive.reset()

    # turn to 45 degree
    drive.turn_to(45)
    assert 42<drive.angle()<48

    drive.turn_to(0)
    assert -2<drive.angle()<2


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

def test_drive():
    drive.reset()
    drive.drive_to(200, 0, 200)
    wait(500)
    print("Distance: ", drive.drive_base.distance())
    # drive.measure_dT()
    # drive.calculate_measures()


# Source: https://fll-pigeons.github.io/gamechangers/gyro_pid.html
def measure_dT()->None:
    watch = StopWatch()
    print("Loop start")

    Ts = 150 # target speed of robot in mm/s

    Kp = 3 #  the Constant 'K' for the 'p' proportional controller

    integral = 0 # initialize
    Ki = 0.025 #  the Constant 'K' for the 'i' integral term

    derivative = 0 # initialize
    lastError = 0 # initialize
    Kd = 3 #  the Constant 'K' for the 'd' derivative term

    count = 0
    for count in range(500):    
        wait(5)
        error = drive.drive_base.angle() # proportional 
        if (error == 0): # prevent the integral term from 'overshooting'
            integral = 0
        else:
            integral = integral + error    
        derivative = error - lastError  
        
        correction = (Kp*(error) + Ki*(integral) + + Kd*derivative) * -1
        
        drive.drive_base.drive(Ts, correction)

        lastError = error  
        
        count = count + 1

    drive.drive_base.stop()

    time = watch.time()
    print("Loop time [s]: " + str(time/1000.0))
    print("Loop iterations: " + str(count))
    print("time per loop (dT): " + str(time/1000.0 / count))


def calculate_measures()->None:
    watch = StopWatch()
    print("Loop start")

    Pc = 0.5 # oscillation period from previous run
    Ns = 1000 # number of steps in loop
    Ts = 150 # target speed of robot in mm/s

    Kp = 5 #  the Constant 'K' for the 'p' proportional controller

    integral = 0 # initialize
    Ki = 0.025 #  the Constant 'K' for the 'i' integral term

    derivative = 0 # initialize
    lastError = 0 # initialize
    Kd = 3 #  the Constant 'K' for the 'd' derivative term

    count = 0
    for count in range(Ns):    
        error = drive.drive_base.angle() # proportional 
        if (error == 0): # prevent the integral term from 'overshooting'
            integral = 0
        else:
            integral = integral + error    
        derivative = error - lastError  
        
        correction = (Kp*(error) + Ki*(integral) + + Kd*derivative) * -1
        
        drive.drive_base.drive(Ts, correction)

        lastError = error  
        
        count = count + 1
        wait(5)

    drive.drive_base.stop()

    time = watch.time()/1000.0

    Kc = Kp
    dT = time / count

    print("Loop time: " + str(time))
    print("Loop iterations: " + str(count))

    Kp = 0.60 * Kc 
    Ki =  2 * Kp * dT / Pc
    Kd = Kp * Pc / (8 * dT)

    print("inputs: Kc=" + str(Kc) + "; dT=" + str(dT) + "; Pc=" + str(Pc))
    print("recommended PID parms: Kp=" + str(Kp) + "; Ki=" + str(Ki) + "; Kd=" + str(Kd))


# test_drive()
measure_dT()

quit()


# sys.exit()


test_turn_to()
test_reset()
   


drive.straigt(700)



# wait(2000)
print(-hub.imu.heading())
# drive.straight(100)
drive.turn(20)
wait(500)
print(-hub.imu.heading())
drive.turn(20)
wait(500)
print(-hub.imu.heading())
drive.turn(20)
wait(500)
print(-hub.imu.heading())
drive.turn(20)
wait(500)
print(-hub.imu.heading())
drive.turn(20)


drive.stop()
# drive.straigt(750)
# drive.turn(90)
# wait(100)
# drive.straigt(600)
# drive.turn(180)
# drive.straigt(600)
# drive.turn(-90)


# drive.straigt(749)
# drive.turn(-90)
# drive.straigt(-100)

# drive.rotate_forward(90)
# wait(2000)
# drive.rotate_forward(-90)
# wait(2000)
# run_task(drehe_auf(90, True, Raeder.RECHTS))
# wait(2000)
# run_task(drehe_auf(-90, True, Raeder.RECHTS))
# wait(2000)
# run_task(drehe_auf(90, True, Raeder.LINKS))
# wait(2000)
# run_task(drehe_auf(-90, True, Raeder.LINKS))

# wait(2000)
# run_task(drehe_auf(45, True, Raeder.LINKS))
# wait(2000)
# run_task(drehe_auf(-45, True, Raeder.LINKS))


# run_task(gyro_fahren(10, 500))

# run_task(gyro_fahren_timeout(10, 500))

# run_task(drehe_auf(90, True))
# wait(2000)
# run_task(drehe_auf(90, False))



wait(10000)

