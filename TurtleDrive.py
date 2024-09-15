from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.parameters import (
 Stop,
 Color,
 Button
)


WHEEL_DIAMETER = 62
AXLE_TRACK = 112


class TurtleDrive:
 def __init__(self, GYRO=True):
  # Initialize both motors. In this example, the motor on the
  # left must turn counterclockwise to make the robot go forward.
  self.left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
  self.right_motor = Motor(Port.B)
  # Initialize the drive base. In this example, the wheel diameter is 56mm.
  # The distance between the two wheel-ground contact points is 112mm.
  self.drive_base = DriveBase(self.left_motor, self.right_motor, wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK)
  
  self.drive_base.use_gyro(GYRO)

 def drive(self, distance=0, wait=True):
   self.drive_base.straight(distance, then=Stop.HOLD, wait=wait)

  def turn(self, angle, wait=True):
    self.drive_base.turn()


