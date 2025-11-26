from TurtleDrive import *
from TurtleAttachement import *
from pybricks.tools import wait, multitask, run_task


# line up left side second dark line from left
def run_market(td, ta):
    td.straight_drive(430)
    ta.move_D_time(speed_percentage=-100, time_millisec=800)
    ta.move_D_time(speed_percentage=100, time_millisec=1000)
    ta.move_D_time(speed_percentage=-100, time_millisec=800)
    ta.move_D_time(speed_percentage=100, time_millisec=1000)
    ta.move_D_time(speed_percentage=-100, time_millisec=1000)
    ta.move_D_time(speed_percentage=100, time_millisec=1000)
    ta.move_D_time(speed_percentage=-100, time_millisec=1000)
    ta.move_D_time(speed_percentage=100, time_millisec=1500)
    td.straight_drive(-290)
    td.turn(-45)
    td.straight_drive(390)

    # FIX: Removed the undefined run_task() wrapper
    ta.move_C_angle(200)

    td.straight_drive(-130)

    # FIX: Removed the undefined run_task() wrapper
    ta.move_C_angle(-200)

    td.straight_drive(-300)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_market(td, ta)
