from pybricks.ev3devices import (Motor)
from essential.Object_creator import left_mission_motor
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from drive_tools.follow_line import follow_line_right
from drive_tools.straight_line import straight_line, straight_line_distance
from drive_tools.turn import turn


def run_2():
    straight_line_distance(0, -100, 2000)
    straight_line_distance(0, 200, 100)
    turn(90, 0)
    straight_line_distance(0, -100, 500)
    turn(-90, 0)
    follow_line_right(-200, 2000)
     straight_line(0, 100, 4000)
    turn(-50, 0)
    straight_line_distance(0, -200, 200)