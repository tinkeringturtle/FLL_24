from TurtleDrive import *
from TurtleAttachement import *


def run():
    td = TurtleDrive()
    # to drive stright do - td.drive(x mm)

    print(td.get_speed())
    td.stright_drive(200)

    td.set_speed(speed=300)
    td.straight_drive(200)

    print(td.get_speed())

    td.turn(-90)
    td.straight_drive(200)
    td.turn(90)


test_distance = 25
test_angle = 90
test_radius = 100


def move(td, curve=0, back=0):
    distance = test_distance
    angle = test_angle
    radius = test_radius
    if back:
        distance = test_distance * -1
        angle = test_angle * -1
        radius = test_radius * -1
    td.straight_drive(distance)
    if curve:
        td.curve(radius, angle)
    else:
        td.turn(angle)


def set_min(td):
    td.set_speed_percentage(0, 0, 0, 0)
    td.get_speed_raw()
    # move(td, 1, 1)


def set_max(td):
    td.set_speed_percentage(100, 100, 100, 100)
    td.get_speed_raw()
    # move(td, 1, 1)


def run2():
    td = TurtleDrive(ENABLE_LOGS=True)
    td.get_speed_raw()

    # Set min speed
    set_min(td)
    # move(td, 1)

    td.turn_drive(500, 5, 5000)
    # set max speed
    # test_max(td)

    td.get_speed_raw()


async def test_attachement(ta):
    await ta.move_C_angle(angle=160, speed_percentage=20)
    ta.move_D_angle(angle=180, speed_percentage=20)
    # ta.move_left_time(speed_percentage=20, time_millisec=3000)
    # ta.move_right_time(speed_percentage=20, time_millisec=3000)


"""
    await multitask(
        ta.move_C_angle(angle=160, speed_percentage=20),
        ta.move_D_angle(angle=180, speed_percentage=20),
    )
"""

## Below doesn't work
# await multitask(
#    ta.move_left_time(speed_percentage=20, time_millisec=3000),
#    ta.move_right_time(speed_percentage=20, time_millisec=3000),
# )


if __name__ == "__main__":
    # run2()
    ta = TurtleAttachment()
    run_task(test_attachement(ta))
