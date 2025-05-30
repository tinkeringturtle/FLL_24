# :turtle: :turtle: :turtle: Tinkering Turtle :turtle: :turtle: :turtle:

## Software to be installed 
* we are using local hosted code server

## VS code Extension
* Error Lens: https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens  
* Git Autoconfig: https://marketplace.visualstudio.com/items?itemName=shyykoserhiy.git-autoconfig 
* GitHub Pull Requests: https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github 
* Pylance: https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance 
* Python: https://marketplace.visualstudio.com/items?itemName=ms-python.python
* Black Formatter: https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter 

## Optional plugins for advance coding
* Auto docstring: https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring 
* GitLens: https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens 
* Live Share: https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare 

## Instruction 
* Each team member creates their own github account. 
* Recommend taking a few extra minutes to set up two-factor authentication. 
* In VS Code add the necessary extensions and restart VS Code. When you restart, you should have the option to Clone a Repository. 
* Clone this repository: 
    https://github.com/tinkeringturtle/FLL_24.git 
* Save the repository somewhere in the computer, recommended to save it in 'My Documents'
* Add a python virtual environment. Press `Ctrl+Shifyt-P` and then type `Python: Create Environment` and select that by clicking

> Alternatively for advance user create the python virtual enviroment as below
> * Open a new terminal with ctrl-shift-`  or Ctrl-Shift-P > Create Terminal 
> * Make sure it is in the python virtual environment. 
> ``` 
> python -m venv .venv 
> ./Scripts/bin/activate.bat
> ```
> * Run the below command to setup the dependencies 
> ```
> python -m pip install -r requirements.txt
> ```

> Note: It will start with a green "(.venv)". If there are executionPolicy errors, you will need to elevate the permissions for 
> Powershell. Instructions here (copied here), but basically just run Set-ExecutionPolicy RemoteSigned in an Administrative PowerShell.

* Create a new python file, named teamMemberName-test-mission.py, copy and paste the code below, and save it, but don't try to run it just yet. Wait for step below. Note that after saving the file, the python Black Formatter should correct the "incorrect" spacing around the equals signs and commas.
* Commit the changes, and push. It will probably prompt for github registration/login and then sync all files. This link may help: https://pages.nist.gov/git-novice-MSE/08-collab/. It may also ask you to set your git username and email. Open a terminal and run these two commands to set your username and email 
```
git config --global user.name "FIRST_NAME LAST_NAME"
git config --global user.email "MY_NAME@example.com"
```

> #### Installing Pybricks on robot 
> Install pybricks on each robot at https://beta.pybricks.com/. If the computer has never connected to a pybricks hub, you will > probably need to manually install the USB drivers, which will require the use of the windows Device Manager. To run device manager as an admin, run a powershell as an administrator, then type devmgmt.msc. Then complete the usual steps. Name the robot at this time. Avoid spaces and special characters in the robot name. Put a label sticker on the top of the robot with the robot name.


* Last step, Add a keyboard shortcut to run the programs that we write. Ctrl-Shift-P > Preferences: Open Keyboard Shortcuts (JSON). Edit the JSON to add the keyboard shortcut to run the task. Paste in the code below at the bottom of keybindings.json.

[
    {
        "key" : "ctrl+shift+l",
        "command" : "workbench.action.tasks.runTask",
        "args": "Run-on-my-robot"
    },
    {
        "key" : "ctrl+alt+l",
        "command" : "workbench.action.tasks.runTask",
        "args": "Run-on-any-robot"
    },
    {
        "key" : "ctrl+shift+r",
        "command" : "workbench.action.tasks.runTask",
        "args": "Run-master_program-on-my-robot"
    },
    {
        "key" : "ctrl+alt+r",
        "command" : "workbench.action.tasks.runTask",
        "args": "Run-master_program-on-any-robot"
    }
]

## RUN PROGRAM ON ROBOT
* Update the ROBOT_NAME file with your robot name.
* Turn the robot on and ensure the keyboard shortcut ctrl-shift-L runs the command, which should also run their program. 
* Also, Ctrl-Alt-L > Tasks: Run task should pop up a menu with the correct entry. Watch the terminal and make sure the robot name is correct. If not, recheck that you completed step 11 correctly

## Refrence
* pybricks https://pybricks.com/ https://code.pybricks.com/ and https://beta.pybricks.com/  
  Nothing to install on your computer, but you will need to install it on your robot.


---

# Coding Documentation
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

### Contributor
* Jessica
* Paige
