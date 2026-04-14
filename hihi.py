from TurtleDrive import *
from TurtleAttachement import *


# from pybricks.tools import wait, multitask, run_task


# line nine
def Run_blank(td, ta):
    print("start run")
    run_task(ta.move_D_angle(150, speed_percentage=60))  # lower arm
    td.straight_drive(590)
    td.turn(-65)
    td.straight_drive(490)
    td.turn(65)  # get flag in
    td.straight_drive(40)
    run_task(ta.move_D_angle(-70, speed_percentage=60))  # pick up Iana
    td.straight_drive(-100)  # back up form Iana
    td.turn(-90)
    td.straight_drive(165)  # 195
    td.turn(-45)  # turn towards seal
    td.straight_drive(195)
    td.straight_drive(-20)
    run_task(ta.move_C_angle(-715, speed_percentage=100))
    run_task(ta.move_C_angle(715, speed_percentage=100))
    td.straight_drive(-130)  # go away form seal

    td.turn(45)
    td.straight_drive(200)
    td.turn(-90)
    run_task(ta.move_D_angle(100, speed_percentage=60))
    td.straight_drive(-40)

    return
    td.straight_drive(400)
    td.curve(300, -50)
    run_task(ta.move_D_angle(200, speed_percentage=60))
    td.turn(-20)
    td.straight_drive(420)
    td.turn(15)  # turn to get the flag in
    td.straight_drive(-80)  # back up form Iana
    return
    td.turn(20)  # turn towords form Iana
    td.straight_drive(80)  # pick up Iana
    run_task(ta.move_D_angle(-200, speed_percentage=60))
    td.straight_drive(-100)  # back up form Iana
    td.turn(-50)  # turn to red side
    td.straight_drive(260)
    td.turn(-55)  # turn towards seal
    td.set_speed_percentage(50)
    td.straight_drive(400)
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
