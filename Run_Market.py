from TurtleDrive import *
from TurtleAttachement import *
from pybricks.tools import run_task


# --- Market Mission ---
def run_market(td, ta):
    # Move forward to start
    td.straight_drive(325)
    # Arm movements
    run_task(ta.move_C_angle(-280, speed_percentage=2000))
    run_task(ta.move_D_angle(-230))
    run_task(ta.move_C_angle(280, speed_percentage=1000))
    # Back up
    td.straight_drive(-110)
    run_task(ta.move_D_angle(225))
    td.set_speed_percentage(100)
    td.straight_drive(-250)

    # You can add extra steps here if needed
    return


# --- IMPORTANT ---
# DO NOT create td or ta here
# DO NOT call run_market(td, ta) here
# The main program will create td and ta and call this function when needed
