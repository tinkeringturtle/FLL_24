from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=95)


# from the left 12th line
# hi


def run_Anshi(td, ta):
    print("start run")
    td.straight_drive(-159)
    td.turn(-90)
    td.straight_drive(-730)
    td.set_speed_percentage(30)
    td.turn(95)
    td.straight_drive(218)
    run_task(ta.move_D_angle(-915))
    wait(5)
    td.straight_drive(-220)
    td.turn(5)
    run_task(ta.move_C_angle(330))
    run_task(ta.move_C_angle(-330))
    td.set_speed_percentage(90)
    td.straight_drive(15)
    td.turn(100)
    td.straight_drive(420)
    td.turn(-35)
    td.straight_drive(615)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Anshi(td, ta)
# run_task(ta.move_C_angle(200))
