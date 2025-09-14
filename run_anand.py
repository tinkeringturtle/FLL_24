from TurtleDrive import *
from TurtleAttachement import *


# line nine
def run_anand(td, ta):
    print("start run")
    td.straight_drive(30)
    td.curve(300,50)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_anand(td, ta)
