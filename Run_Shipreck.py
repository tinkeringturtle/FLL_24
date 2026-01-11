from TurtleDrive import *
from TurtleAttachement import *

# from pybricks.tools import wait, multitask, run_task


# line up at 1st black line
# line nine
def run_Shipreck(td, ta):
    print("start run")
    td.set_speed_percentage(66)
    td.straight_drive(475)
    td.set_speed_percentage(10)
    run_task(ta.move_D_angle(-140))
    td.set_speed_percentage(100)
    td.straight_drive(-175)
    run_task(ta.move_D_angle(150))
    td.straight_drive(-450)


# Main Function
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Shipreck(td, ta)
