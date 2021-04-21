from pybricks.ev3devices import (Motor)
from essential.Object_creator import left_mission_motor
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from drive_tools.straight_line import straight_line
from drive_tools.follow_line import follow_line_left, follow_line_right

def run_4():
    follow_line_right(-100, 1000)