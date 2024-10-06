# Tinkering Turtle 


## TrutleDrive.py : Main motor class

td = TurtleDrive()

1. staright_drive(__distance_mm__)
2.  turn(__angle_deg_) ## Its a pivot turn
3.  curve(__radius_mm__, __angle__deg__)
4.  set_speed_percentage(
        speed_percentage,
        acceleration_percentage,
        turn_rate_percentage,
        turn_acceleration_percentage,
    ):

td.set_speed_settings(speed_percentage=10)
td.set_speed_settings(accerlation_percentage=10,turn_accerlation=25)


## TurtleAttachement.py : Main attachement Class

ta = TurtleAttachement()

ta.move_c_angle()

1. move_D_angle(
        angle=0,
        speed_percentage=DEFAULT_ATTACHEMNET_SPEED_PERCENTAGE,
    ):
2. move_C_angle(
        angle=0,
        speed_percentage=DEFAULT_ATTACHEMNET_SPEED_PERCENTAGE,
    ):
 
 
 def move_D_time(
        self, speed_percentage=DEFAULT_ATTACHEMNET_SPEED_PERCENTAGE, time_millisec=500
    ):
        


### Gearsbot robot siimulation https://github.com/QuirkyCort/gears 