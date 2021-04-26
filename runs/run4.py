from pybricks.ev3devices import (Motor)
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor, right_mission_motor, left_mission_motor
from drive_tools.straight_line import straight_line, straight_line_distance, straight_line_light_black, straight_line_light_white
from drive_tools.follow_line import follow_line_left, follow_line_right, follow_line_distance_left, follow_line_distance_right
from drive_tools.turn import turn
from pybricks.tools import wait
def run_4():
    straight_line_distance(0, -200, 50)
    straight_line_distance(-45, -100, 550)
    straight_line_distance(-90, -100, 100)
    straight_line_distance(-90, -100, 235)
    straight_line_distance(-90, 100, 50)
    turn(-125, 2)
    wait(100)
    straight_line_distance(-130, -100, 150)
    right_mission_motor.run_time(-400, 4500)
    right_mission_motor.run_time(200, 4000)
    straight_line_distance(-130, 100, 200)
    straight_line_distance(-40, -100, 220)
    straight_line_distance(-40, 100, 20)
    straight_line_distance(-40, -100, 20)
    straight_line_distance(-40, 100, 20)
    straight_line_distance(-40, -100, 20)
    straight_line_distance(-40, 100, 20)
    straight_line_distance(-40, -100, 20)
    straight_line_distance(-40, 100, 20)
    straight_line_distance(-40, -100, 20)
    straight_line_distance(-40, 100, 20)
    straight_line_distance(-40, -100, 20)
    straight_line_distance(-40, 100, 20)
    straight_line_distance(-40, -100, 20)






    
    
    
    
    
    #straight_line_distance(-35, -100, 400)
    #follow_line_distance_left(-80, 400)
    
    
    
    
    
    
    
    
    
    
    
    #straight_line_distance(0, -200, 40)
    #follow_line_distance_right(100, 300)
    #straight_line_distance(52, -200, 510)
    #straight_line_distance(0, -300, 200)
    #follow_line_distance_right(-100, 150)
    
    #straight_line_distance(0, -100, 250)