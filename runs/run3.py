from pybricks.ev3devices import (Motor)
from essential.Object_creator import left_mission_motor
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from pybricks.tools import wait

def run_3():
    left_mission_motor.run(-800)
    