from TurtleDrive import *
from TurtleAttachement import *



def Run_Test(td, ta):
    print("start run")
    td.straight_drive(500) 
    


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_Test(td, ta)