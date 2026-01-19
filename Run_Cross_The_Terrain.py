from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from TurtleDrive import *
from TurtleAttachement import *

# from pybricks.tools import wait, multitask, run_task


# line up on line 2 form the right
def run_Anshi(td, ta):

    print("start run")
    td.set_speed_percentage(60)
    td.straight_drive(-170)
    td.set_speed_percentage(75)
    td.turn(-90)
    td.straight_drive(-200)
    return
    td.straight_drive(-715)
    td.set_speed_percentage(50)
    td.turn(95)
    td.straight_drive(265)
    td.turn(-15)
    run_task(ta.move_D_angle(-325.5))  # spins Angler Artifact
    td.straight_drive(40)
    run_task(ta.move_D_angle(-325.5))
    td.turn(-9)
    td.straight_drive(-150)
    td.turn(16)
    td.straight_drive(-180)
    td.turn(-9)  # grabs seabead sample
    td.set_speed_percentage(90)
    td.straight_drive(240)  # exits seabead area
    td.turn(-57.67)
    run_task(ta.move_C_angle(-525, speed_percentage=90))  # arm goes down
    td.set_speed_percentage(60)
    td.straight_drive(-225)  # gose into seal
    td.turn(30)
    td.turn(-30)
    td.straight_drive(130)
    td.turn(-40)
    td.set_speed_percentage(100)
    td.straight_drive(-240)
    td.turn(-40)
    td.straight_drive(-670)
    return
    td.turn(11)
    td.straight_drive(-185)  # appraoches seal
    td.turn(5)
    td.set_speed_percentage(80)
    td.straight_drive(-45)
    td.turn(-8)
    # run_task(ta.move_C_angle(150, speed_percentage=50))  # arm goes up; seal goes up
    run_task(ta.move_C_angle(150, speed_percentage=35))  # arm goes up; seal goes up
    td.straight_drive(150)
    td.turn(-40)
    td.straight_drive(-850)  # heads toward anshi area


# MAIN FUNCTION
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Anshi(td, ta)

# skbidi toiler will be mine yeah ohio gyatt rizz, rizzler on my mind yeah. 67im gving up on you, ill 41 if you want me tooo anwhere i would have mustard youuu u 67 im givin gup on youuuuuuuu..
