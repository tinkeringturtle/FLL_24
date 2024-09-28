from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task

# Set up all devices.
left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B)
gripper_left = Motor(Port.C)
gripper_right = Motor(Port.D)


drive_base = DriveBase(left, right, 56, 114)


# Move the gripper up and down.
async def move_gripper():
    await gripper_left.run_angle(500, -90)
    await gripper_left.run_angle(500, 90)


# Drive forward, turn move gripper at the same time, and drive backward.
async def main():
    await drive_base.straight(250)
    await multitask(drive_base.turn(90), move_gripper())
    await drive_base.straight(-250)


async def move_attachment(left, right):
    await multitask(left.run_angle(500, -90), right.run_angle(500, 90))


# Runs the main program from start to finish.
run_task(move_attachment(gripper_left, gripper_right))
