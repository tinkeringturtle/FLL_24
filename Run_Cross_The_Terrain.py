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
    td.straight_drive(-715)
    td.set_speed_percentage(50)
    td.turn(95)
    td.straight_drive(240)
    run_task(ta.move_D_angle(-635))  # spins Angler Artifact
    td.turn(-9)
    td.straight_drive(-295)
    td.turn(-8)  # grabs seabead sample
    td.set_speed_percentage(90)
    td.straight_drive(195)  # exits seabead area
    td.turn(-59)
    run_task(ta.move_C_angle(-525, speed_percentage=90))  # arm goes down
    td.set_speed_percentage(70)
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
