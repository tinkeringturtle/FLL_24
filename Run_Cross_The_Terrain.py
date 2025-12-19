from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=100)


# from the left 12th line
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
    td.straight_drive(260)
    td.turn(-7)
    run_task(ta.move_D_angle(-920))
    wait(8)
    td.set_speed_percentage(30)
    td.straight_drive(100)
    td.turn(-8)
    td.straight_drive(-220)
    # td.turn(-50)
    td.set_speed_percentage(85)
    run_task(ta.move_C_angle(355))
    run_task(ta.move_C_angle(-355))
    td.straight_drive(125)
    td.set_speed_percentage(75)
    td.turn(-65)
    td.straight_drive(-200)
    td.turn(-45)
    td.straight_drive(-800)

    return
    td.set_speed_percentage(30)
    td.turn(100)
    td.straight_drive(150)
    td.turn(50)
    td.straight_drive(500)
    td.turn(-25)
    td.straight_drive(50)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Anshi(td, ta)
# run_task(ta.move_C_angle(200))
