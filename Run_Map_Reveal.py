from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)


# line nine
def run_Map_Reveal(td, ta):
    print("start run")
    td.set_speed_percentage(100)
    #run_task(ta.move_C_angle(60))
    #run_task(ta.move_C_angle(100))
    #run_task(ta.move_C_angle(235))
    td.straight_drive(705)
    td.set_speed_percentage(25)
    td.straight_drive(-155)
    run_task(ta.move_C_angle(150))
    wait(1.5)
    td.set_speed_percentage(100)
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
    td.curve(-100,-90)
    td.straight_drive(-7000)
   
    
    

if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Map_Reveal(td, ta)
