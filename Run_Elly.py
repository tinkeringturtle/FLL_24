from TurtleDrive import *
from TurtleAttachement import *


# line nine
def Run_Elly(td, ta):
    print("start run")
    td.straight_drive(500)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_Elly(td, ta)