def get_col():
    data = fs.hsv()
    h, s, v = data.h, data.s, data.v

    # 1. Very dark is still Black (v < 12)
    if v <= 12:
        return "BLACK"

    # 2. This is the new "Gray/None" zone.
    # If it's between 13 and 30, we tell it to ignore it (NONE)
    # so it doesn't accidentally run the Black mission.
    if 13 <= v <= 30 and s <= 20:
        return "NONE"

    # 3. White needs to be very bright
    if v >= 65 and s <= 30:
        return "WHITE"

    # 4. Other colors
    if 180 <= h <= 280 and s > 35:
        return "BLUE"
    if (h <= 15 or h >= 345) and s > 45:
        return "RED"

    return "NONE"
