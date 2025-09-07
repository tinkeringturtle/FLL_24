from TurtleDrive import *
from TurtleAttachement import *


# line nine
def run_bolders(td, ta):
    print("start run")
    td.straight_drive(725)
    #td.curve(10,100)
    td.turn(-90)
    td.straight_drive(100)
    td.turn(30)
    td.straight_drive(-100)
    td.turn(-30)
    td.straight_drive(-200)
    td.straight_drive(200)

if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_bolders(td, ta)

