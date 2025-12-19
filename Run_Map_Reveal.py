from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)


# line nine
def run_Map_Reveal(td, ta):
    print("start run")
    td.set_speed_percentage(85)
    td.straight_drive(705)  # Go to get brush
    td.straight_drive(-175)
    td.straight_drive(45)
    run_task(ta.move_C_angle(230))
    run_task(ta.move_C_angle(-220))
    run_task(ta.move_C_angle(230))
    return
    run_task(ta.move_D_angle(150))
    wait(1.5)
    td.set_speed_percentage(100)
    td.turn(20)
    td.straight_drive(305)
    td.turn(-78)
    td.turn(13.5)
    td.straight_drive(250)
    td.straight_drive(-45)
    td.set_speed_percentage(100)
    run_task(ta.move_D_angle(-150))
    td.set_speed_percentage(100)
    td.straight_drive(-150)
    td.curve(-100, -60)
    td.set_speed_percentage(100)
    td.straight_drive(-700)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Map_Reveal(td, ta)
