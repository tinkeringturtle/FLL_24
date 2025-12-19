from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Assuming these files and functions exist in your project
from TurtleDrive import *
from TurtleAttachement import *
import Run_Cross_The_Terrain, Run_artifact, Run_Bolders
import Run_Map_Reveal, Run_Market, Run_Seal_Deliver, Run_Shipreck
import Run_silo

# ----------------------------------------------------------------------
# --- SENSOR INITIALIZATION ---
# ----------------------------------------------------------------------
hub = PrimeHub()
bottom_sensor = ColorSensor(Port.E)
front_sensor = ColorSensor(Port.F)

# ----------------------------------------------------------------------
# --- 1. CUSTOM HSV RANGES (FINAL CALIBRATION) ---
# ----------------------------------------------------------------------

# --- BLACK ---
BLACK_SAT_MAX = 20
BLACK_VAL_MAX = 15

# --- WHITE (Captures very dark, desaturated gray/off-white) ---
WHITE_SAT_MAX = 25
WHITE_VAL_MIN = 16

# --- ORANGE ---
ORANGE_HUE_MIN = 0
ORANGE_HUE_MAX = 45
ORANGE_SAT_MIN = 50
ORANGE_VAL_MIN = 40

# --- LIGHT_GREEN ---
LIGHT_GREEN_HUE_MIN = 85
LIGHT_GREEN_HUE_MAX = 110
LIGHT_GREEN_SAT_MIN = 30
LIGHT_GREEN_VAL_MIN = 40

# --- DARK_GREEN (Named GREEN - H:158 fix) ---
GREEN_HUE_MIN = 110
GREEN_HUE_MAX = 170
GREEN_SAT_MIN = 40
GREEN_VAL_MIN = 20

# --- BLUE ---
BLUE_HUE_MIN = 190
BLUE_HUE_MAX = 270
BLUE_SAT_MIN = 50
BLUE_VAL_MIN = 20

# ----------------------------------------------------------------------
# --- 2. STREAMLINED DETECTION FUNCTION ---
# ----------------------------------------------------------------------


def get_detected_color(color_data):
    """Checks the current HSV reading against the defined mission ranges."""
    h = color_data.h
    s = color_data.s
    v = color_data.v

    # 1. CHECK BLACK
    if v <= BLACK_VAL_MAX and s <= BLACK_SAT_MAX:
        return "BLACK"

    # 2. CHECK WHITE/GRAY
    if v >= WHITE_VAL_MIN and s <= WHITE_SAT_MAX:
        return "WHITE"

    # 3. CHECK ORANGE
    hue_orange_ok = (h >= ORANGE_HUE_MIN) and (h <= ORANGE_HUE_MAX)
    sat_val_orange_ok = (s >= ORANGE_SAT_MIN) and (v >= ORANGE_VAL_MIN)
    if hue_orange_ok and sat_val_orange_ok:
        return "ORANGE"

    # 4. CHECK LIGHT_GREEN
    hue_light_green_ok = (h >= LIGHT_GREEN_HUE_MIN) and (h <= LIGHT_GREEN_HUE_MAX)
    sat_val_light_green_ok = (s >= LIGHT_GREEN_SAT_MIN) and (v >= LIGHT_GREEN_VAL_MIN)
    if hue_light_green_ok and sat_val_light_green_ok:
        return "LIGHT_GREEN"

    # 5. CHECK DARK_GREEN (Named GREEN)
    hue_green_ok = (h >= GREEN_HUE_MIN) and (h <= GREEN_HUE_MAX)
    sat_val_green_ok = (s >= GREEN_SAT_MIN) and (v >= GREEN_VAL_MIN)
    if hue_green_ok and sat_val_green_ok:
        return "GREEN"

    # 6. CHECK BLUE
    hue_blue_ok = (h >= BLUE_HUE_MIN) and (h <= BLUE_HUE_MAX)
    sat_val_blue_ok = (s >= BLUE_SAT_MIN) and (v >= BLUE_VAL_MIN)
    if hue_blue_ok and sat_val_blue_ok:
        return "BLUE"

    return "UNKNOWN"


# ----------------------------------------------------------------------
# --- 3. MAIN PROGRAM LOOP ---
# ----------------------------------------------------------------------

print(
    "Brainrot compilation: Tralaleo tralla, ballerina capuchina, tung tung tung sahur, los tralaritos, lirri lirri larrila, trippi troppi, assasino bandito. The End. Part 2 coming soon!"
)

td = TurtleDrive()
ta = TurtleAttachment()

# --- START-GATE WAIT LOOP ---
hub.light.on(Color.BLUE)
while (
    Button.RIGHT not in hub.buttons.pressed()
    and Button.LEFT not in hub.buttons.pressed()
):
    wait(10)

hub.light.off()
print("--- STARTING MISSION ---")


# Main mission loop for color detection and mission triggering
while True:
    hsv_data = front_sensor.hsv()
    detected_color = get_detected_color(hsv_data)
    buttons_pressed = hub.buttons.pressed()

    # Check which buttons are being held down
    is_right_pressed = Button.RIGHT in buttons_pressed
    is_left_pressed = Button.LEFT in buttons_pressed

    # ------------------------------------------------------------------
    # --- 1. PRIORITY MISSIONS (Requires Color AND Button Press) ---
    # ------------------------------------------------------------------

    # --- WHITE MISSION (SIMULTANEOUS DUAL BUTTON LOGIC) ---
    if detected_color == "WHITE":
        if is_right_pressed:
            print("White + Right Button: RUNNING BOLDERS!")
            td.stop()
            hub.light.on(Color.YELLOW)
            Run_Bolders.run_bolders(td, ta)
            # Wait for button release, then continue loop (program doesn't stop)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)
            hub.light.off()

        elif is_left_pressed:
            print("White + Left Button: RUNNING MARKET!")
            td.stop()
            hub.light.on(Color.YELLOW)
            Run_Market.run_market(td, ta)
            # Wait for button release, then continue loop (program doesn't stop)
            while Button.LEFT in hub.buttons.pressed():
                wait(10)
            hub.light.off()

    # --- DARK_GREEN MISSION ---
    elif detected_color == "GREEN" and is_right_pressed:
        print("Dark Green + Button: RUNNING MAP REVEAL!")
        td.stop()
        hub.light.on(Color.WHITE)
        Run_Map_Reveal.run_Map_Reveal(td, ta)
        while is_right_pressed:
            wait(10)
        hub.light.off()

    # --- LIGHT_GREEN MISSION ---
    elif detected_color == "LIGHT_GREEN" and is_right_pressed:
        print("Light Green + Button: RUNNING SHIPRECK!")
        td.stop()
        hub.light.on(Color.GREEN)
        Run_Shipreck.run_Shipreck(td, ta)
        while is_right_pressed:
            wait(10)
        hub.light.off()

    # --- ORANGE MISSION ---
    elif detected_color == "ORANGE" and is_right_pressed:
        print("Orange + Button: RUNNING SEAL DELIVER!")
        td.stop()
        hub.light.on(Color.ORANGE)
        Run_Seal_Deliver.Run_Seal_Deliver(td, ta)
        while is_right_pressed:
            wait(10)
        hub.light.off()

    # --- BLUE MISSION ---
    elif detected_color == "BLUE" and is_right_pressed:
        print("Blue + Button: RUNNING CROSS THE TERRAIN (ANSHI)!")
        td.stop()
        hub.light.on(Color.BLUE)
        Run_Cross_The_Terrain.run_Anshi(td, ta)
        while is_right_pressed:
            wait(10)
        hub.light.off()

    # ------------------------------------------------------------------
    # --- 2. INSTANT MISSION (Color Only) ---
    # ------------------------------------------------------------------

    # --- BLACK MISSION ---
    elif detected_color == "BLACK":
        print("Black detected: RUNNING ARTIFACT (ALICE)!")
        td.stop()
        hub.light.off()
        Run_artifact.Run_Alice(td, ta)
        # Wait for button release just in case, then continue the loop.
        while is_right_pressed or is_left_pressed:
            wait(10)

    # ------------------------------------------------------------------
    # --- 3. CATCH-ALL FEEDBACK (Indicates Detected Color, Waiting for Button) ---
    # ------------------------------------------------------------------

    # WHITE - Light YELLOW, waiting for button
    elif detected_color == "WHITE":
        # The light only turns on if we are waiting for a button press.
        hub.light.on(Color.YELLOW)

    # DARK GREEN (GREEN) - Light WHITE, waiting for button
    elif detected_color == "GREEN":
        hub.light.on(Color.WHITE)

    # LIGHT GREEN - Light GREEN, waiting for button
    elif detected_color == "LIGHT_GREEN":
        hub.light.on(Color.GREEN)

    # ORANGE - Light ORANGE, waiting for button
    elif detected_color == "ORANGE":
        hub.light.on(Color.ORANGE)

    # BLUE - Light BLUE, waiting for button
    elif detected_color == "BLUE":
        hub.light.on(Color.BLUE)

    # All other colors (including UNKNOWN) result in no light
    else:
        hub.light.off()

    wait(50)
