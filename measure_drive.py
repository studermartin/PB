from pybricks.tools import wait
from pybricks.tools import StopWatch
from drive import drive
from hub import hub
from hub import wait_for_button_pressed

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

# print(drive.__straight_deceleration())
quit()
