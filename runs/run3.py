from pybricks.ev3devices import Motor
from essential.Object_creator import left_mission_motor, gyro
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from pybricks.tools import wait
from drive_tools.straight_line import straight_line, straight_line_distance, straight_line_light_black
from drive_tools.turn import turn
from essential.Object_creator import DriveBase
from essential.Object_creator import right_mission_motor


def run_3():
  gyro.reset_angle(0)
  # straight_line_light_black(0, -1000, right_color_sensor)
  straight_line_distance(-20, -100, 30)
  straight_line_distance(0, -200, 870)
  turn(-90, 2)
  straight_line_distance(-20, -100, 140)
  straight_line_distance(-90, 100, 60)
  straight_line_distance(-90, -100, 500)
  straight_line_distance(-35, -100, 90)
  straight_line_distance(-35, 100, 65)
  straight_line_distance(-60, -100, 70)
  turn(-190, 2)
  right_mission_motor.run_time(200, 1000)
  straight_line_distance(-215, 100, 70)
  straight_line_distance(-215, -500, 100)
  DriveBase.stop()