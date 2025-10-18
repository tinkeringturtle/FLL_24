from TurtleDrive import *
from TurtleAttachement import *


def set_speed_percentage(
    self,
    speed_percentage=DEFAULT_SPEED_PERCENTAGE,
    acceleration_percentage=DEFAULT_ACCELERATION_PERCENTAGE,
    turn_rate_percentage=DEFAULT_TURN_RATE_PERCENTAGE,
    turn_acceleration_percentage=DEFAULT_TURN_ACCELERATION_PERCENTAGE,
):

    async def runAttachemnt(ta, angle):
        await ta.move_C_angle(angle=angle, speed_percentage=20)


# this is the code for the attachment: run_task(ta.move_D_angle(90))
# code for looping motor: for i in range(10)
#   run_task(ta.move_D_angle(-300))


# line nine
def Run_Seal_Deliver(td, ta):
    print("start run")
    # run starts here
    td.straight_drive(217)
    td.set_speed_percentage(turn_rate_percentage=30)
    td.curve(90, 67)
    td.set_speed_percentage(40)  # slowing down
    td.straight_drive(270)  # going into the area
    run_task(ta.move_D_angle(300))  # lowering arm
    td.straight_drive(100)
    run_task(ta.move_D_angle(-500))  # lifting arm
    td.set_speed_percentage(20)
    # td.straight_drive(-50)  # drive back a little bit slowly
    td.set_speed_percentage(100)  # speed up
    # td.straight_drive(-350)  # drive back at full speed


# run ends here
if __name__ == "__main__":
    print(
        "the italian brainrot compliation #1 by meghana: tralalao tralala, ballerina capuchina, tung tung tung sahur, bombadilo crocadilo, grenadila gorila,trippi troopa, lirili larila, brr brr patapim, tung tung assasenio boneca, Cacasito La vaca Trippa troppa Bombombini Gusini Tralala Lirilira Tung Satelito Tung Sahur boneka Tung Tung tralalelo cappuccino assasine Tirilikalika Trippi Trenostruzzo Turbo 3000 troppa Crocodina fruli Crocodildo Penosini frulia Bublito Bandito Traktorito. Thats all the brainrot that i know. JK i know more. Part 2 coming soon."
    )
    # i love italian brainrot #tralaleotralala
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_Seal_Deliver(td, ta)
