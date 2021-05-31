from pybricks.ev3devices import Motor
from essential.Object_creator import left_mission_motor, gyro
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from pybricks.tools import wait
from drive_tools.straight_line import straight_line, straight_line_distance, straight_line_light_black
from drive_tools.turn import turn
from essential.Object_creator import drive_base
from essential.Object_creator import right_mission_motor, left_mission_motor
from drive_tools.follow_line import follow_line_distance_left, follow_line_distance_right, follow_line_left, follow_line_right
from pybricks.tools import wait
from pybricks.parameters import Button

def run_3():
  gyro.reset_angle(0)
  straight_line_distance(-15, -200, 200)
  follow_line_distance_right(-150, 960)
  drive_base.stop()
  wait(305)
  straight_line_distance(-60, 150, 290)
  straight_line_distance(-85, -250, 150)
  follow_line_distance_right(-170, 415)
  straight_line_distance(-90, -150, 200)
  left_mission_motor.run_time(500, 2000)
  straight_line_distance(-90, 180, 200)
  straight_line_distance(-35, -180, 75)
  straight_line_distance(-35, 180, 120)
  straight_line_distance(-60, -180, 140)
  turn(-190, 2)
  right_mission_motor.run_time(300, 1800)
  straight_line_distance(-245, 180, 80)
  straight_line_distance(-220, -500, 170)
  straight_line_distance(-195, 250, 250)
  straight_line_distance(-180, -250, 300)
  straight_line_distance(-210, -20000, 1000)
  