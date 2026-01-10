from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon, Port, Color
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait

# Assuming these files and functions exist in your project
from TurtleDrive import *
from TurtleAttachement import *
import Run_Cross_The_Terrain, Run_artifact, Run_Bolders
import Run_Map_Reveal, Run_Market, Run_Forum_Plus_Flags, Run_Shipreck
import Run_silo

# ----------------------------------------------------------------------
# --- SENSOR INITIALIZATION ---
# ----------------------------------------------------------------------
hub = PrimeHub()
bottom_sensor = ColorSensor(Port.E)
front_sensor = ColorSensor(Port.F)

# ----------------------------------------------------------------------
# --- 1. CUSTOM HSV RANGES (CALIBRATED) ---
# ----------------------------------------------------------------------

# --- BLACK ---
BLACK_SAT_MAX = 20
BLACK_VAL_MAX = 15

# --- WHITE ---
WHITE_SAT_MAX = 25
WHITE_VAL_MIN = 16

# --- ORANGE ---
ORANGE_HUE_MIN = 0
ORANGE_HUE_MAX = 45
ORANGE_SAT_MIN = 50
ORANGE_VAL_MIN = 40

# --- LIGHT_GREEN (UPDATED FOR HUE 84) ---
LIGHT_GREEN_HUE_MIN = 70  # Lowered to catch your reading
LIGHT_GREEN_HUE_MAX = 100
LIGHT_GREEN_SAT_MIN = 30
LIGHT_GREEN_VAL_MIN = 30

# --- DARK_GREEN (Named GREEN) ---
GREEN_HUE_MIN = 110  # Gap created between 100 and 110
GREEN_HUE_MAX = 170
GREEN_SAT_MIN = 40
GREEN_VAL_MIN = 20

# --- BLUE ---
BLUE_HUE_MIN = 190
BLUE_HUE_MAX = 270
BLUE_SAT_MIN = 50
BLUE_VAL_MIN = 20

# ----------------------------------------------------------------------
# --- 2. DETECTION FUNCTION ---
# ----------------------------------------------------------------------


def get_detected_color(color_data):
    h = color_data.h
    s = color_data.s
    v = color_data.v

    if v <= BLACK_VAL_MAX and s <= BLACK_SAT_MAX:
        return "BLACK"
    if v >= WHITE_VAL_MIN and s <= WHITE_SAT_MAX:
        return "WHITE"

    # Check Hues
    if (h >= ORANGE_HUE_MIN) and (h <= ORANGE_HUE_MAX) and s >= ORANGE_SAT_MIN:
        return "ORANGE"
    if (
        (h >= LIGHT_GREEN_HUE_MIN)
        and (h <= LIGHT_GREEN_HUE_MAX)
        and s >= LIGHT_GREEN_SAT_MIN
    ):
        return "LIGHT_GREEN"
    if (h >= GREEN_HUE_MIN) and (h <= GREEN_HUE_MAX) and s >= GREEN_SAT_MIN:
        return "GREEN"
    if (h >= BLUE_HUE_MIN) and (h <= BLUE_HUE_MAX) and s >= BLUE_SAT_MIN:
        return "BLUE"

    return "UNKNOWN"


# ----------------------------------------------------------------------
# --- 3. MAIN PROGRAM ---
# ----------------------------------------------------------------------

td = TurtleDrive()
ta = TurtleAttachment()

hub.light.on(Color.BLUE)
print("Waiting for Button to start...")

while not any(hub.buttons.pressed()):
    wait(10)

hub.light.off()
print("--- MISSION SELECTOR ACTIVE ---")

while True:
    hsv_data = front_sensor.hsv()
    detected_color = get_detected_color(hsv_data)
    buttons = hub.buttons.pressed()

    # --- WHITE MISSIONS ---
    if detected_color == "WHITE":
        if Button.RIGHT in buttons:
            print("RUNNING BOLDERS")
            td.stop()
            hub.light.on(Color.YELLOW)
            Run_Bolders.run_bolders(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)
        elif Button.LEFT in buttons:
            print("RUNNING MARKET")
            td.stop()
            hub.light.on(Color.YELLOW)
            Run_Market.run_market(td, ta)
            while Button.LEFT in hub.buttons.pressed():
                wait(10)
        else:
            hub.light.on(Color.YELLOW)

    # --- DARK GREEN (MAP REVEAL) ---
    elif detected_color == "GREEN":
        if Button.RIGHT in buttons:
            td.stop()
            hub.light.on(Color.WHITE)
            Run_Map_Reveal.run_Map_Reveal(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)
        else:
            hub.light.on(Color.WHITE)

    # --- LIGHT GREEN (SHIPRECK) ---
    elif detected_color == "LIGHT_GREEN":
        if Button.RIGHT in buttons:
            td.stop()
            hub.light.on(Color.GREEN)
            Run_Shipreck.run_Shipreck(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)
        else:
            hub.light.on(Color.GREEN)

    # --- ORANGE (FORUM) ---
    elif detected_color == "ORANGE":
        if Button.RIGHT in buttons:
            td.stop()
            hub.light.on(Color.ORANGE)
            Run_Forum_Plus_Flags.Run_Forum_Plus_Flags(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)
        else:
            hub.light.on(Color.ORANGE)

    # --- BLUE (CROSS TERRAIN) ---
    elif detected_color == "BLUE":
        if Button.RIGHT in buttons:
            td.stop()
            hub.light.on(Color.BLUE)
            Run_Cross_The_Terrain.run_Anshi(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)
        else:
            hub.light.on(Color.BLUE)

    # --- BLACK (ARTIFACT - INSTANT) ---
    elif detected_color == "BLACK":
        td.stop()
        hub.light.off()
        Run_artifact.Run_Alice(td, ta)
        while any(hub.buttons.pressed()):
            wait(10)

    else:
        hub.light.off()

    wait(50)
