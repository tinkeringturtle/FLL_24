from TurtleDrive import *
from TurtleAttachement import *
async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)
#from the left 12th line 

def run_Anshi(td, ta):
    print("start run")
    td.straight_drive(-100)
    td.turn(-90)
    td.straight_drive(-525)
    td.turn(90)
    td.straight_drive(30)
    


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Anshi(td, ta)
#run_task(ta.move_C_angle(200))