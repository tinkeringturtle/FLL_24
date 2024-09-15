from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.parameters import (
 Stop,
 Color,
 Button
)

WHEEL_DIAMETER = 62.4
AXLE_TRACK = 128

SPEED = 216
ACCELERATION = 811
TURN_RATE = 184
TURN_ACCELERATION=830

class TurtleDrive:
  def __init__(self, GYRO=True):
    # Initialize both motors. In this example, the motor on the
    # left must turn counterclockwise to make the robot go forward.
    self.left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    self.right_motor = Motor(Port.B)
    # Initialize the drive base. In this example, the wheel diameter is 56mm.
    # The distance between the two wheel-ground contact points is 112mm.
    self.drive_base = DriveBase(self.left_motor, self.right_motor, wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK)
    #self.set_speed()
    self.drive_base.use_gyro(GYRO)

    # add attachement motor 

    # add color sensor
    #self.e_color=ColorSensor(Port.E)
    #self.f_color=ColorSensor(Port.F)

  """
  drive the robot straight to spcified distance 
  """
  def drive(self, distance=0, wait=True):
    self.drive_base.straight(distance, then=Stop.HOLD, wait=wait)


  """
  Turns the robot to an specified angle
  positive angle turen to the right, negative angle 
  turn to left
  """
  def turn(self, angle, wait=True):
    self.drive_base.turn(angle, then=Stop.HOLD, wait=wait)

  """
  Get the speed setting in tuple(straight_speed, straing_aceel, turn_speed, turn_accel)
  """
  def get_speed(self):
    return self.drive_base.settings()
  
  def set_speed(self, speed=SPEED, acceleration=ACCELERATION, turn_rate=TURN_RATE, turn_acceleration=TURN_ACCELERATION):
    self.drive_base.settings(speed, acceleration, turn_rate, turn_acceleration)


