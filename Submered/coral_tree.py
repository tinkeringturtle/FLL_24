# Author: Nitya, Paige

from TurtleDrive import *
from TurtleAttachement import *


def CoralTree(td, ta):
    td.straight_drive(350)
    td.set_speed_percentage(speed_percentage=25, acceleration_percentage=10)
    td.straight_drive(50)
    td.turn(-15)
    td.turn(30)
    td.turn(-15)
    td.set_speed_percentage(speed_percentage=75, acceleration_percentage=50)
    td.straight_drive(-385)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    CoralTree(td, ta)
