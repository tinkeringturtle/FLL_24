from TurtleDrive import *
from TurtleAttachement import *


# line nine
def run_Shipreck(td, ta):
    print("start run")
    td.set_speed_percentage(100)
    td.straight_drive(700)
    td.straight_drive(-100)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Shipreck(td, ta)
