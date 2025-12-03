from TurtleDrive import *
from TurtleAttachement import *
from pybricks.tools import wait, multitask, run_task


# line up left side second dark line from left
def run_market(td, ta):
    td.straight_drive(250)
    td.turn(-50)
    td.straight_drive(245)
    run_task(ta.move_C_angle(200))  # dropiing for market
    td.set_speed_percentage(20)
    td.straight_drive(-150)
    td.set_speed_percentage(50)
    td.straight_drive(20)
    run_task(ta.move_C_angle(-200))  # lift
    td.turn(10)
    td.straight_drive(-80)  # change to get the right position for the lever
    run_task(ta.move_C_angle(215))  # dropping for lever
    td.straight_drive(30)  # the go forward before moving the lever
    td.turn(-45)  # lever hits, this is where we turn to activate the lever thing
    td.turn(35)

    td.straight_drive(-350)
    run_task(ta.move_C_angle(-200))
    # ta.move_D_time(speed_percentage=-100, time_millisec=800)  # 1 hit
    # ta.move_D_time(speed_percentage=100, time_millisec=1000)  # 1 hit
    # ta.move_D_time(speed_percentage=-100, time_millisec=800)  # 2 hit
    # ta.move_D_time(speed_percentage=100, time_millisec=1000)  # 2 hit
    # ta.move_D_time(speed_percentage=-100, time_millisec=1000)  # 3 hit
    # ta.move_D_time(speed_percentage=100, time_millisec=1000)  # 3 hit
    # ta.move_D_time(speed_percentage=-100, time_millisec=1000)  # 4 hit
    # ta.move_D_time(speed_percentage=100, time_millisec=1500)  # 4 hit
    # td.straight_drive(-400)  # back home


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_market(td, ta)
