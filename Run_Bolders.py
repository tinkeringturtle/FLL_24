from TurtleDrive import *
from TurtleAttachement import *


# line nine
def run_bolders(td, ta):
    print("start run")
    td.straight_drive(725)
    #td.curve(10,100)
    td.turn(-100)
    #wait(500) instead of waiting, turn less than -90 (maybe -60), drive straight a little and then rest of the turn
    td.straight_drive(100)
    td.turn(30)
    td.straight_drive(-90)
    td.turn(-30)
    td.straight_drive(-200)
    td.turn(10)
    td.straight_drive(650)
    td.turn(22)
    td.straight_drive(-200)
    td.straight_drive(100)
    td.turn(-5)
    td.straight_drive(-200)
    td.turn(40)
    td.straight_drive(-700)
    

if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_bolders(td, ta)

