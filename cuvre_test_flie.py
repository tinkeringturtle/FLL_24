from TurtleDrive import *
from TurtleAttachement import *


# line nine
def run_Test(td, ta):
    print("start run")
    td.curve(385,113)
    

if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Test(td, ta)