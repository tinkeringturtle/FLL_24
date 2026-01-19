from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Port, Color
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait
from TurtleDrive import *
from TurtleAttachement import *

# Mission Imports
import Run_Cross_The_Terrain, Run_artifact, Run_Bolders
import Run_Map_Reveal, Run_Market, Run_Forum_Plus_Flags, Run_Shipreck
import A_Toast_To_Treasure

# SENSOR INITIALIZATION
hub = PrimeHub()
front_sensor = ColorSensor(Port.F)

# CALIBRATED HSV RANGES
BLACK_SAT_MAX, BLACK_VAL_MAX = 20, 15
WHITE_SAT_MAX, WHITE_VAL_MIN = 25, 70


def get_detected_color(color_data):
    h, s, v = color_data.h, color_data.s, color_data.v
    # PRIORITY 1: RED
    if (h <= 10 or h >= 350) and s >= 50 and v >= 30:
        return "RED"
    # PRIORITY 2: BLACK
    if v <= BLACK_VAL_MAX and s <= BLACK_SAT_MAX:
        return "BLACK"
    # PRIORITY 3: BLUE
    if (200 <= h <= 250) and s >= 50:
        return "BLUE"
    # PRIORITY 4: YELLOW
    if (46 <= h <= 80) and s >= 50:
        return "YELLOW"
    # PRIORITY 5: WHITE
    if v >= WHITE_VAL_MIN and s <= WHITE_SAT_MAX:
        return "WHITE"
    return "UNKNOWN"


td = TurtleDrive()
ta = TurtleAttachment()

# --- INITIAL START ---
hub.light.on(Color.BLUE)
while not any(hub.buttons.pressed()):
    wait(10)
hub.speaker.beep()
hub.light.off()

# --- MAIN LOOP ---
while True:
    color = get_detected_color(front_sensor.hsv())
    pressed = hub.buttons.pressed()

    # Visual Feedback: Light up the hub based on what it SEES
    if color == "RED":
        hub.light.on(Color.RED)
    elif color == "BLUE":
        hub.light.on(Color.BLUE)
    elif color == "YELLOW":
        hub.light.on(Color.YELLOW)
    elif color == "BLACK":
        hub.light.on(Color.VIOLET)  # Violet means it sees Black/Artifact
    else:
        hub.light.off()

    # ACTION: Only run if a button is pressed
    if Button.RIGHT in pressed:
        td.stop()  # Force stop any existing movement

        if color == "RED":
            A_Toast_To_Treasure.run_Elly(td, ta)
        elif color == "YELLOW":
            Run_Bolders.run_bolders(td, ta)
        elif color == "BLUE":
            Run_Cross_The_Terrain.run_Anshi(td, ta)
        elif color == "BLACK":
            Run_artifact.Run_Alice(td, ta)

        # Wait for button release
        while any(hub.buttons.pressed()):
            wait(10)

    elif Button.LEFT in pressed:
        if color == "WHITE":
            td.stop()
            Run_Market.run_market(td, ta)
            while any(hub.buttons.pressed()):
                wait(10)

    wait(50)
