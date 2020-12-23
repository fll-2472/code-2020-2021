from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch

BLACK = 6
WHITE = 70
setpoint = (BLACK + WHITE) / 2

K_P = 3.65

def follow_line(speed, duration, drive_base, color_sensor):
    while timer.time() <duration:
        deviation = color_sensor.reflection() - setpoint

        turn_rate = K_P * deviation

        drive_base.drive(speed, turn_rate)

        wait(10)
