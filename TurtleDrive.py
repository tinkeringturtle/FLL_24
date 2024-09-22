from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.parameters import Stop, Color, Button
from TurtleConstant import *


DEFUALT_MIN_SPEED_MMSEC = 20  # it can be set to 0, setting 25 as lowest speed
DEFAULT_MAX_SPEED_MMSEC = 800  #

DEFAULT_MIN_ACCELERATION_MMSEC = 20
DEFAULT_MAX_ACCELERATION_MMSEC = 800

DEFAULT_MIN_TURN_RATE_DEGSEC = 20
DEFAULT_MAX_TURN_RATE_DEGSEC = 180

DEFAULT_MIN_TURN_ACCELERATION_DEGSEC2 = 20
DEFAULT_MAX_TURN_ACCELERATION_DEGSEC2 = 360


class TurtleDrive:
    def __init__(self, ENABLE_GYRO=True):
        # Initialize both motors. In this example, the motor on the
        # left must turn counterclockwise to make the robot go forward.
        self.left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.B)
        # Initialize the drive base. In this example, the wheel diameter is 56mm.
        # The distance between the two wheel-ground contact points is 112mm.
        self.drive_base = DriveBase(
            self.left_motor,
            self.right_motor,
            wheel_diameter=WHEEL_DIAMETER,
            axle_track=AXLE_TRACK,
        )
        self.set_speed_setting()
        self.use_gyro(ENABLE_GYRO)

        # add attachement motor
        # TODO:

        # add color sensor
        # TODO:
        # self.e_color=ColorSensor(Port.E)
        # self.f_color=ColorSensor(Port.F)

    def use_gyro(self, enable=True):
        self.drive_base.use_gyro(enable)

    """
    drive the robot straight to spcified distance 
    """

    def straight_drive(self, distance=0, wait=True):
        self.drive_base.straight(distance, then=Stop.HOLD, wait=wait)

    def turn_drive(self, speed, turn_rate, time_millis, wait=True):
        self.drive_base.drive(speed, turn_rate)
        wait(time_millis)

    """
    Turns the robot to an specified angle
    positive angle turen to the right, negative angle 
    turn to left
    """

    def turn(self, angle, wait=True):
        self.drive_base.turn(angle, then=Stop.HOLD, wait=wait)

    def curve(self, radius, angle, wait=True):
        self.drive_base.curve(radius, angle, then=Stop.HOLD, wait=wait)

    """
    Get the speed setting in tuple(straight_speed, straing_aceel, turn_speed, turn_accel)
    """

    def percentage_to_value(self, percentage_value, max_actual_value):
        negative = False
        if percentage_value < 0:
            negative = True
        percentage_value = abs(percentage_value)
        if percentage_value < 0:
            percentage_value = 0
        if percentage_value > 100:
            percentage_value = 100

        speed_mmsec = (percentage_value / 100) * max_actual_value
        if negative == True:
            return speed_mmsec * -1
        else:
            return speed_mmsec

    def get_speed_mmsec(self, percentage_value):
        return self.percentage_to_value(self, percentage_value, DEFAULT_MAX_SPEED_MMSEC)

    def get_acceleration_mmsec2(self, percentage_value):
        return self.percentage_to_value(
            percentage_value, DEFAULT_MAX_ACCELERATION_MMSEC
        )

    def get_turn_rate_degsec(self, percentage_value):
        return self.percentage_to_value(percentage_value, DEFAULT_MAX_TURN_RATE_DEGSEC)

    def get_turn_acceleration_degsec2(self, percentage_value):
        return self.percentage_to_value(
            percentage_value, DEFAULT_MAX_TURN_ACCELERATION_DEGSEC2
        )

    def get_speed_settings(self):
        return self.drive_base.settings()

    def set_speed_settings(
        self,
        speed_percentage=DEFAULT_SPEED_PERCENTAGE,
        acceleration_percentage=DEFAULT_ACCELERATION_PERCENTAGE,
        turn_rate_percentage=DEFAULT_TURN_RATE_PERCENTAGE,
        turn_acceleration_percentage=DEFAULT_TURN_ACCELERATION_PERCENTAGE,
    ):
        speed = self.get_speed_mmsec(speed_percentage)
        acceleration = self.get_acceleration_mmsec2(acceleration_percentage)
        turn_rate = self.get_turn_rate_degsec(turn_rate_percentage)
        turn_acceleration = self.get_turn_acceleration_degsec2(
            turn_acceleration_percentage
        )
        self.drive_base.settings(speed, acceleration, turn_rate, turn_acceleration)
