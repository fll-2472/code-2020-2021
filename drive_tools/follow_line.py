from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch

BLACK = 9
WHITE = 86
threshold = (BLACK + WHITE) / 2

PROPORTIONAL_GAIN = 1.2

def follow_line(speed, duration, drive_base, color_sensor):
    while timer.time() <duration:
        deviation = color_sensor.reflection() - threshold

        turn_rate = PROPORTIONAL_GAIN * deviation

        drive_base.drive(speed, turn_rate)

        wait(10)
