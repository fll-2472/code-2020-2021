from pybricks.ev3devices import (Motor)
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor, right_mission_motor, left_mission_motor
from drive_tools.straight_line import straight_line, straight_line_distance, straight_line_light_black, straight_line_light_white
from drive_tools.follow_line import follow_line_left, follow_line_right, follow_line_distance_left, follow_line_distance_right
from drive_tools.turn import turn
from pybricks.tools import wait
from essential.Object_creator import gyro

def run_4():
    gyro.reset_angle(0)
    straight_line_distance(0, -200, 250)
    straight_line_distance(-90, -200, 530)
    left_mission_motor.run_time(-40000, 2500)
    left_mission_motor.run_time(40000, 2500)
    straight_line_distance(-30, -100, 170)
    turn(-90, 2)
    straight_line_distance(-90, -100, 85)
    straight_line_distance(-90, 100, 70)
    turn(-110, 2)
    wait(100)
    straight_line_distance(-135, -120, 175)
    right_mission_motor.run_time(-400, 4500)
    right_mission_motor.run_time(2000, 1000)
    straight_line_distance(-130, 150, 240)
    straight_line_distance(-40, -170, 330)

    while True:
        straight_line_distance(-40, 100, 20)
        straight_line_distance(-40, -100, 20)
        straight_line_distance(-40, 100, 40)
        straight_line_distance(-40, -100, 40)


    # straight_line_distance(0, -200, 50)
    # straight_line_distance(-45, -150, 557)
    # wait(100)
    # straight_line_distance(-90, -100, 100)
    # straight_line_distance(-90, -150, 243)
    # straight_line_distance(-90, 100, 80)
    # turn(-120, 2)
    # wait(100)
    # straight_line_distance(-130, -120, 200)
    # right_mission_motor.run_time(-400, 4500)
    # right_mission_motor.run_time(200, 4500)
    # straight_line_distance(-130, 150, 240)
    # straight_line_distance(-40, -170, 370)

    # while True:
    #     straight_line_distance(-40, 100, 20)
    #     straight_line_distance(-40, -100, 20)
    #     straight_line_distance(-40, 100, 40)
    #     straight_line_distance(-40, -100, 40)




