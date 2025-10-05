from TurtleDrive import *
from TurtleAttachement import *


# line nine
def run_bolders(td, ta):
    print("start run")
    td.straight_drive(710) #725
    td.turn(-60)
    td.straight_drive(25)
    td.turn(35)
    td.straight_drive(30)
    td.turn(90)
    td.straight_drive(-90)
    td.turn(-90)
    td.set_speed_percentage(20)
    td.straight_drive(-260)
    td.set_speed_percentage(75)
    td.straight_drive(220)
    td.turn(-90)
    td.straight_drive(750)

def run_market(td, ta):
    td.straight_drive(250)
    td.turn(-48)
    td.straight_drive(200)
    run_task(ta.move_C_angle(180))
    td.straight_drive(40)
    td.straight_drive(-120)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    #run_bolders(td, ta)
    run_market(td, ta)

