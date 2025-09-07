from TurtleDrive import *
from TurtleAttachement import *

async def runAttachemnt(ta, angle):
    await ta.move_C_angle(angle=angle, speed_percentage=40)

# line nine
def Run_Seal_Jones(td, ta):
    print("start run")

#Run starts here
    
#Run ends here




 #run_task(runAttachemnt(ta, 180))
    #run_task(runAttachemnt(ta, -180))

if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_Seal_Jones(td, ta)
