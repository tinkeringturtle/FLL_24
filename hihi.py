from TurtleDrive import *
from TurtleAttachement import *


# from pybricks.tools import wait, multitask, run_task


# line nine
def Run_blank(td, ta):
    print("start run")
    td.straight_drive(400)
    td.curve(300, -50)
    run_task(ta.move_D_angle(250, speed_percentage=60))
    td.turn(-15)
    td.straight_drive(420)
    td.turn(20)
    td.straight_drive(-115)  # back up form Iana
    td.turn(20)
    td.straight_drive(80)
    return
    td.turn(-50)
    td.straight_drive(345)
    td.turn(-40)
    td.straight_drive(160)
    run_task(ta.move_C_angle(-699, speed_percentage=100))
    td.straight_drive(-100)
    run_task(ta.move_C_angle(699, speed_percentage=100))
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
