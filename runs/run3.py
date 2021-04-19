from pybricks.ev3devices import (Motor)
from essential.Object_creator import left_mission_motor, gyro
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from pybricks.tools import wait
from drive_tools.straight_line import straight_line, straight_line_distance, straight_line_light_black
from drive_tools.turn import turn

def run_3():
  gyro.reset_angle(0)
 # straight_line_light_black(0, -1000, right_color_sensor)
  straight_line_distance(0, -100, 900)
  turn(-90, 2)
  straight_line_distance(-80, -100, 80)
  straight_line_distance(-90, -100, 200)