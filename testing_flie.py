from TurtleDrive import *
from TurtleAttachement import *


# line nine
def Run_Test(td, ta):
    print("start run")
    #Test starts here
    td.straight_drive(500)
    #td.straight_drive(-500)
    #Test ends here

if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_Test(td, ta)
