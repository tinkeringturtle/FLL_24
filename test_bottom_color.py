from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from TurtleDrive import *
from TurtleAttachement import *

# Initialize sensor
sensor = ColorSensor(Port.E)


def detect_bottom_color(td):
    # 1. Measure the 'White' floor before moving
    starting_brightness = sensor.hsv().v
    # Define black as 30% darker than the start
    threshold = starting_brightness * 0.7

    print("Starting Brightness:", starting_brightness)
    print("Target Threshold:", threshold)

    # 2. Start moving forward
    td.turn_drive(100, 0, 0)

    while True:
        current_v = sensor.hsv().v

        if current_v < threshold:
            td.stop()
            print("Detected Black!")
            break

        wait(10)


def run_Anshi(td, ta):
    # Mission Steps
    td.straight_drive(-460)
    td.straight_drive(1060)

    # Line Detection
    detect_bottom_color(td)

    # Full stop before turn
    td.stop()
    wait(500)

    # Final Turn
    td.set_speed_percentage(50)
    td.turn(45)
    run_task(ta.move_D_angle(-500))
    td.straight_drive(200)
    td.straight_drive(-180)
    run_task(ta.move_D_angle(500))
    td.turn(-60)
    td.straight_drive(300)
    td.turn(-50)
    td.straight_drive(300)


# --- Main Execution ---
td = TurtleDrive()
ta = TurtleAttachment()

# Call the function ONLY ONCE so it doesn't restart and move back
run_Anshi(td, ta)
