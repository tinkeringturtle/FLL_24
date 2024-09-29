from TurtleDrive import *


def run():
    td = TurtleDrive()
    print(td.get_speed_settings())
    # to drive stright do - td.drive(x mm)
    # td.set_speed(turn_rate=100, turn_acceleration=350)  # for sunset
    # td.set_speed(speed=544, acceleration=5000)
    # td.set_speed(acceleration=10)
    td.turn_drive(110, 184, 500)
    print(td.get_speed_settings())
    # td.turn(90)
    # td.curve(radius=500, angle=360)


run()
