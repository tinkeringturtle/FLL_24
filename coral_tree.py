# Author: Nitya, Page

from TurtleDrive import *
from TurtleAttachement import *


def CoralTree(td, ta):

    td.set_speed_percentage(65)
    td.straight_drive(-10)
    td.straight_drive(455)
    ta.move_C_time(speed_percentage=25, time_millisec=3200)
    td.straight_drive(-385)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    CoralTree(td, ta)
