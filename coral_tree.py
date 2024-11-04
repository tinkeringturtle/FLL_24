# Author: Nitya, Page

from TurtleDrive import *
from TurtleAttachement import *


def CoralTree(td, ta):

    td.straight_drive(-10)
    td.straight_drive(400)
    td.turn(-15)
    td.turn(15)
    td.turn(-15)
    td.turn(15)
    td.straight_drive(-385)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    CoralTree(td, ta)
