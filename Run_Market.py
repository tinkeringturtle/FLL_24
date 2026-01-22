from TurtleDrive import *
from TurtleAttachement import *
from pybricks.tools import wait, multitask, run_task

# from pybricks.tools import wait, multitask, run_task


# line up left side second dark line from left
def run_market(td, ta):

    td.straight_drive(325)  # going forward
    run_task(
        ta.move_C_angle(-280, speed_percentage=2000)
    )  # arm to get the artifact thing,
    run_task(ta.move_D_angle(-220))  # market and lever
    ta.move_C_angle(270, speed_percentage=1000)
    # arm to get the artifact thing back
    td.straight_drive(-100)
    run_task(ta.move_D_angle(225))
    td.set_speed_percentage(100)
    td.straight_drive(-250)

    return
    td.straight_drive(250)
    td.turn(-50)
    td.straight_drive(255)
    run_task(ta.move_C_angle(200))  # dropiing for market
    td.set_speed_percentage(20)
    td.straight_drive(15)
    td.straight_drive(-150)
    td.set_speed_percentage(50)
    td.straight_drive(20)
    run_task(ta.move_C_angle(-200))  # lift
    td.straight_drive(-50)
    # td.turn(10)
    td.straight_drive(-100)  # change to get the right position for the lever
    run_task(ta.move_C_angle(180))  # dropping for lever
    td.straight_drive(85)  # the go forward before moving the lever
    td.turn(-45)  # lever hits, this is where we turn to activate the lever thing
    td.turn(35)

    td.straight_drive(-400)


# run_task(ta.move_C_angle(-200))


if __name__ == "__main__":
    print("Hello")
td = TurtleDrive()
ta = TurtleAttachment()
run_market(td, ta)
