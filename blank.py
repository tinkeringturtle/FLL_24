from TurtleDrive import *
from TurtleAttachement import *


# from pybricks.tools import wait, multitask, run_task


# line nine
def Run_blank(td, ta):
    print("start run")
    td.straight_drive(150)
    td.curve(530, -50)
    # wait(1000)
    td.straight_drive(380)
    td.turn(20)
    td.straight_drive(20)  # turn to get flag in
    td.straight_drive(80)
    td.straight_drive(-100)  # back up form Iana
    td.turn(-70)
    td.straight_drive(320)
    td.turn(-40)
    td.straight_drive(140)
    run_task(ta.move_C_angle(-999, speed_percentage=100))
    return
    td.turn(-90)
    td.straight_drive(445)
    td.turn(-35)
    td.straight_drive(100)
    run_task(ta.move_D_angle(-250))
    return
    td.straight_drive(200)
    td.curve(530, -70)
    td.straight_drive(260)
    td.turn(60)
    run_task(ta.move_D_angle(-130))
    td.straight_drive(30)
    run_task(ta.move_D_angle(130))


# Main Function
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_blank(td, ta)
