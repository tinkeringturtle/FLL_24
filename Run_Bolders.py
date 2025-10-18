from TurtleDrive import *
from TurtleAttachement import *


# line nine
def run_bolders(td, ta):
    print("start run")
    td.straight_drive(725) #725
    td.turn(-60)
    td.straight_drive(30)
    td.turn(-35)
    td.straight_drive(60)
    td.turn(90)
    td.straight_drive(-90)
    td.turn(-90)
    td.set_speed_percentage(20)
    td.straight_drive(-260)
    td.set_speed_percentage(75)
    td.straight_drive(160)
    td.turn(-47)
    td.straight_drive(370)
    td.straight_drive(-100)
    td.turn(-70)
    td.straight_drive(450)

def run_market(td, ta):
    td.straight_drive(420) 
    ta.move_D_time(speed_percentage=-100, time_millisec=800)
    ta.move_D_time(speed_percentage=100, time_millisec=1000)
    ta.move_D_time(speed_percentage=-100, time_millisec=800)
    ta.move_D_time(speed_percentage=100, time_millisec=1000)
    ta.move_D_time(speed_percentage=-100, time_millisec=800)
    ta.move_D_time(speed_percentage=100, time_millisec=1000)
    ta.move_D_time(speed_percentage=-100, time_millisec=800)
    ta.move_D_time(speed_percentage=100, time_millisec=1000)
    #td.straight_drive(240)
    #td.turn(-48), 
    #td.straight_drive(280)
    #run_task(ta.move_C_angle(200))
    #td.straight_drive(40)
    #td.straight_drive(-150)
    #td.straight_drive(100)
    #run_task(ta.move_C_angle(-180))
    #td.straight_drive(-300)
   


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    #run_bolders(td, ta)
    run_market(td, ta)

