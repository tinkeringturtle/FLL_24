from TurtleDrive import *
from TurtleAttachement import *


# from pybricks.tools import wait, multitask, run_task


# line nine
def Run_blank(td, ta):
    print("start run")

    td.straight_drive(150)
    td.curve(530, -50)
    # run_task(ta.move_D_angle(-125))  # lower arm down
    # wait(1000)
    td.straight_drive(380)
    # run_task(ta.move_D_angle(125))
    # td.turn(10)
    # run_task(ta.move_D_angle(30))  # pick up Iana
    td.straight_drive(30)

    td.straight_drive(-45)

    td.turn(-45)
    td.straight_drive(195)
    td.turn(-35)
    td.set_speed_percentage(60)
    td.straight_drive(100)
    # run_task(ta.move_D_angle(-250))
    td.straight_drive(200)
    td.turn(-20)
    run_task(ta.move_C_angle(-600))
    td.turn(20)
    run_task(ta.move_C_angle(-600))


# Main Function
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_blank(td, ta)
