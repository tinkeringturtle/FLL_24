from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=100)


# from the left 12th line
# hi


def run_Anshi(td, ta):
    print("start run")
    td.straight_drive(-135)
    td.turn(-90)
    td.straight_drive(-695)
    td.set_speed_percentage(50)
    td.turn(95)
    td.straight_drive(250)
    run_task(ta.move_D_angle(-920))
    wait(5)
    td.straight_drive(-235)
    td.turn(-18)
    td.set_speed_percentage(100)
    run_task(ta.move_C_angle(355))
    run_task(ta.move_C_angle(-355))
    td.set_speed_percentage(85)
    td.straight_drive(10)
    td.turn(80)
    td.straight_drive(450)
    td.turn(-10)
    td.straight_drive(500)
    td.turn(-25)
    td.straight_drive(50)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Anshi(td, ta)
# run_task(ta.move_C_angle(200))
