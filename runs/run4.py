from pybricks.ev3devices import (Motor)
from essential.Object_creator import left_mission_motor
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from drive_tools.straight_line import straight_line, straight_line_distance, straight_line_light_black, straight_line_light_white
from drive_tools.follow_line import follow_line_left, follow_line_right, follow_line_distance_left, follow_line_distance_right
from drive_tools import turn
def run_4():
    straight_line_distance(0, -200, 40)
    straight_line_distance(52, -200, 510)
    straight_line_distance(0, -300, 200)
    follow_line_distance_right(-100, 150)
    
    #straight_line_distance(0, -100, 250)