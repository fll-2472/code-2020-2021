from pybricks.ev3devices import (Motor)
from essential.Object_creator import left_mission_motor
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from drive_tools.straight_line import straight_line

def run_4():
    straight_line(0, -100, 1500)
    straight_line(0, 100, 1500)