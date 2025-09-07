from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)

# line nine
def run_Map_Reveal(td, ta):
    print("start run")
    td.set_speed_percentage(100)
    td.straight_drive(720)
    td.set_speed_percentage(7)
    td.turn(-60)
    td.set_speed_percentage(35)
    td.straight_drive(200)
    td.curve(-180, -75)
    td.set_speed_percentage(100)
    td.straight_drive(-100)
    td.set_speed_percentage(50)
    td.straight_drive(230)
    td.curve(50, -60)
    td.straight_drive(20)
    run_task(ta.move_D_angle(-180))
    td.curve(-50, -60)
    td.set_speed_percentage(100)
    td.straight_drive(-1000)

   
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Map_Reveal(td, ta)
