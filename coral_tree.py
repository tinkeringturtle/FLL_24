# Author: Nitya, Paige

from TurtleDrive import *
from TurtleAttachement import *


def CoralTree(td, ta):
    td.straight_drive(-10)
    td.straight_drive(390)
    td.turn(20)
    td.turn(-40)
    td.turn(20)
    # td.turn(-40)
    # td.turn(20)
    td.straight_drive(-385)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    CoralTree(td, ta)
