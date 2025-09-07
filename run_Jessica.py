from TurtleDrive import *
from TurtleAttachement import *


def run_Jessica(td, ta):
    print("start run")
    td.straight_drive(100)
    td.curve(200, 90)
    td.turn(90)


if __name__ == "__main__":
    print("hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Jessica(td, ta)
