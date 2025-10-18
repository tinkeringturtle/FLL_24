from TurtleDrive import *
from TurtleAttachement import *
async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=100)
#from the left 12th line 

def run_Anshi(td, ta):
    print("start run")
    td.straight_drive(-130)
    td.turn(-90)
    td.straight_drive(-700)
    td.turn(95)
    td.straight_drive(160)
    run_task(ta.move_D_angle(-1000))
    td.set_speed_percentage(55)
    td.straight_drive(-185)
    td.straight_drive(160)
    td.straight_drive(20)
    td.curve(-80,100)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Anshi(td, ta)
#run_task(ta.move_C_angle(200))