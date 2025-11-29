from TurtleDrive import *
from TurtleAttachement import *
from pybricks.tools import wait, multitask, run_task


# line nine
def run_bolders(td, ta):
    print("start run")
    td.straight_drive(725)  # 725
    td.turn(-60)
    td.straight_drive(30)  # boulders
    td.turn(-35)
    td.straight_drive(77)  # market thing
    td.turn(90)
    td.straight_drive(-90)
    td.turn(-93)  # going for boulders angle
    td.set_speed_percentage(20)
    td.straight_drive(-270)  # going in for boulders
    td.set_speed_percentage(75)
    td.straight_drive(160)  # coming out
    td.turn(-51)  # change for the lever hting
    td.straight_drive(370)  # hit the lever
    td.straight_drive(-100)
    td.turn(-70)  # back up
    td.straight_drive(470)  # going home


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_bolders(td, ta)
