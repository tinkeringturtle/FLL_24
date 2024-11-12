# Author: Nitya, Page

from TurtleDrive import *
from TurtleAttachement import *


def CoralTree(td, ta):

    td.set_speed_percentage(60)
    td.straight_drive(-10)
    td.straight_drive(500)
    run_task(ta.move_C_angle(angle=-40, speed_percentage=15))
    td.straight_drive(-385)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    CoralTree(td, ta)
