from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)


# line nine
def run_Map_Reveal(td, ta):
    print("start run")
    td.set_speed_percentage(100)
    run_task(ta.move_C_angle(325))
    td.straight_drive(690)
    td.straight_drive(-175)
    td.turn(20)
    td.straight_drive(215)
    td.turn(-78)
    td.turn(15)
    td.straight_drive(250)
    td.straight_drive(-35)
    td.set_speed_percentage(100)
    run_task(ta.move_D_angle(-150))
    td.set_speed_percentage(100)
    td.straight_drive(-200)
    run_task(ta.move_C_angle(-30))
    td.curve(-100,-100)
    td.straight_drive(-25)
    td.turn(-20)
    td.straight_drive(6)
    run_task(ta.move_C_angle(90))
    
    

if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Map_Reveal(td, ta)
