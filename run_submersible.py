# Anshi, Alice

from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_C_angle(angle=angle, speed_percentage=50)

def run_submersible(td, ta):
    print("f")



if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_submersible(td, ta)

