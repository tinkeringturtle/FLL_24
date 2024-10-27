# Author: Nitya, Page

from TurtleDrive import *
from TurtleAttachement import *


def CoralTree(td, ta):

    td.straight_drive(370)
    td.straight_drive(-371)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    CoralTree(td, ta)
