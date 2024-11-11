# Author: Nitya, Paige

from TurtleDrive import *
from TurtleAttachement import *


def CoralTree(td, ta):

    td.straight_drive(-10)
    td.straight_drive(400)
    run_task(ta.move_C_angle(angle=-50, speed_percentage=15))
    run_task(ta.move_C_angle(angle=-100, speed_percentage=35))
    td.straight_drive(-385)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    CoralTree(td, ta)
