from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Assuming these files and functions exist in your project
from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=100)


# from the left 11th line
# hi


def run_Anshi(td, ta):
    print("start run")
    td.set_speed_percentage(60)
    td.straight_drive(-167)
    td.set_speed_percentage(75)
    td.turn(-90)
    td.straight_drive(-715)
    td.set_speed_percentage(50)
    td.turn(95)
    td.straight_drive(245)
    run_task(ta.move_D_angle(-650))
    wait(5)
    td.turn(-8)
    td.straight_drive(-183)
    td.turn(-8)
    td.set_speed_percentage(90)
    td.straight_drive(115)
    td.turn(-65)
    td.straight_drive(-182)
    td.turn(25)
    run_task(ta.move_C_angle(360))
    td.straight_drive(-15)
    run_task(ta.move_C_angle(-360))
    return
    wait(10)
    td.straight_drive(70)
    td.turn(-70)
    td.set_speed_percentage(100)
    td.straight_drive(-767.67)


# td.turn(-50)
# td.straight_drive(-200)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Anshi(td, ta)
