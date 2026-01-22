from TurtleDrive import *
from TurtleAttachement import *

# from pybricks.tools import wait, multitask, run_task


# line nine
def run_Map_Reveal(td, ta):
    print("start run")
    td.set_speed_percentage(85)
    td.straight_drive(565)  # Go to get brush
    run_task(ta.move_C_angle(750))
    run_task(ta.move_C_angle(-750))
    td.turn(45)
    td.straight_drive(220)
    td.turn(-91)  # about to go into map reveal like in front of it
    td.set_speed_percentage(45)
    td.straight_drive(301.5)
    run_task(ta.move_D_angle(-120))
    td.straight_drive(-125)
    td.turn(50)
    td.set_speed_percentage(1000)
    td.straight_drive(-700)
    run_task(ta.move_D_angle(121))

    return
    td.straight_drive(-200)
    run_task(ta.move_C_angle(90))
    td.set_speed_percentage(95)
    td.straight_drive(88.5)
    run_task(ta.move_C_angle(-140))
    run_task(ta.move_C_angle(100))  # should have brush
    wait(1.5)
    td.set_speed_percentage(50)
    td.turn(35)
    td.straight_drive(175)
    td.turn(-80)  # about to go into 3 thing

    td.straight_drive(253)
    td.straight_drive(-15)
    td.set_speed_percentage(100)
    run_task(ta.move_D_angle(-100))
    td.set_speed_percentage(100)
    td.straight_drive(-150)
    td.curve(-100, -60)
    td.set_speed_percentage(100)
    td.straight_drive(-700)


# Main Function
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Map_Reveal(td, ta)
