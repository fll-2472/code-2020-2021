from pybricks.ev3devices import (Motor)
from essential.Object_creator import left_mission_motor
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from pybricks.tools import wait
from drive_tools.straight_line import straight_line, straight_line_distance

def run_3():
  straight_line_distance(0, -20, 700)
    