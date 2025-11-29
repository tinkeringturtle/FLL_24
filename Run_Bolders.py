from TurtleDrive import *
from TurtleAttachement import *
from pybricks.tools import wait, multitask, run_task


# line nine
def run_bolders(td, ta):
    print("start run")
    td.straight_drive(725)  # 725
    td.turn(-55)
    td.straight_drive(30)
    td.turn(-30)
    td.straight_drive(75)  # getting market
    td.turn(30)
    td.straight_drive(-80)
    td.turn(-30)
    td.set_speed_percentage(20)
    td.straight_drive(-240)  # pushing in boulders
    td.set_speed_percentage(75)
    td.straight_drive(160)
    td.turn(-52)
    # td.straight_drive(370)
    # td.straight_drive(-100)
    # td.turn(-70)
    # td.straight_drive(450)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_bolders(td, ta)
