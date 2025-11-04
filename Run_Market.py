from TurtleDrive import *
from TurtleAttachement import *


# line up left side second dark line from left
def run_market(td, ta):
    td.straight_drive(195)
    td.turn(-45)
    td.straight_drive(335)
    run_task(ta.move_C_angle(200))

    # td.straight_drive(40)
    td.straight_drive(-130)
    run_task(ta.move_C_angle(-200))

    # td.straight_drive(120)
    # run_task(ta.move_C_angle(-200))
    # td.straight_drive(-300)
    # td.stop(200)

    # td.straight_drive(420)
    # ta.move_D_time(speed_percentage=-100, time_millisec=800)
    # ta.move_D_time(speed_percentage=100, time_millisec=1000)
    # ta.move_D_time(speed_percentage=-100, time_millisec=800)
    # ta.move_D_time(speed_percentage=100, time_millisec=1000)
    # ta.move_D_time(speed_percentage=-100, time_millisec=800)
    # ta.move_D_time(speed_percentage=100, time_millisec=1000)
    # ta.move_D_time(speed_percentage=-100, time_millisec=800)
    # ta.move_D_time(speed_percentage=100, time_millisec=1500)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_market(td, ta)
