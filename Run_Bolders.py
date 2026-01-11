from TurtleDrive import *
from TurtleAttachement import *

# from pybricks.tools import wait, multitask, run_task


# line up on line nine
def run_bolders(td, ta):
    print("start run")
    td.straight_drive(690)  # 725
    td.turn(-20)
    td.turn(-70)  # hits boulders
    td.straight_drive(70)  # market
    td.straight_drive(-100)  # lil backup
    td.set_speed_percentage(20)
    td.straight_drive(-150)  # going in for boulders
    ta.move_C_time(speed_percentage=100, time_millisec=1000)  # 1 hit
    ta.move_C_time(speed_percentage=-100, time_millisec=1000)  # 1 hit
    ta.move_C_time(speed_percentage=100, time_millisec=1000)  # 1 hit
    ta.move_C_time(speed_percentage=-100, time_millisec=1000)  # 1 hit
    ta.move_C_time(speed_percentage=100, time_millisec=1000)  # 1 hit
    ta.move_C_time(speed_percentage=-100, time_millisec=1000)  # 1 hit
    td.straight_drive(-46.7)
    ta.move_D_time(speed_percentage=100, time_millisec=500)  # 1 hit
    td.straight_drive(-70)
    td.set_speed_percentage(50)
    td.straight_drive(-226.7)
    #  CODE WE DONT USE ANYMORE ,BUT MIGHT NEED AGIAN
    # td.set_speed_percentage(100)
    # td.straight_drive(-160)
    # td.set_speed_percentage(75)
    # td.straight_drive(160)  # coming out
    # td.turn(-51)  # change for the lever hting
    # td.straight_drive(370)  # hit the lever
    # td.straight_drive(-100)
    # td.turn(-70)  # back up
    # td.straight_drive(470)  # going home


# MAIN FUNCTION
if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_bolders(td, ta)
