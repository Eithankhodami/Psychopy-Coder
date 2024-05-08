"""
Author: M. Ahsan Khodami
Update: 2024/05/08
ORCID: https://orcid.org/0000-0003-0130-7752

This code is designed to detect the number of monitors connected to the system and create a window on the primary monitor.
The code uses the screeninfo library to detect the number of monitors and their dimensions. 
If a single monitor is detected, the code uses the dimensions of that monitor to create a window. 
If multiple monitors are detected, the code uses the dimensions of the primary monitor to create a window.

The code uses screeninfo library, if you dont have it install first, using the following command:
pip install screeninfo
NOTE: code is tested with Psychopy 2023.x.x versions.
"""
from psychopy import visual
from screeninfo import get_monitors

def close_existing_screens():
    open_windows = visual.Window.listWindows()
    for window in open_windows:
        window.close()

monitors = list(get_monitors())

if len(monitors) == 1:
    monitor = monitors[0]
    MonitorWidth = monitor.width
    MonitorHeight = monitor.height
    print("Single monitor detected.")
    print("Width:", MonitorWidth)
    print("Height:", MonitorHeight)
elif len(monitors) >= 2:
    for monitor in monitors:           
        if monitor.is_primary:          # Check if the monitor is the primary monitor >>> if it is not primary, you have to add 'not' before 'monitor.is_primary' >> `if not monitor.is_primary:`
            MonitorWidth = monitor.width
            MonitorHeight = monitor.height
            print("Multiple monitors detected. Using primary monitor.")
            print("Width:", MonitorWidth)
            print("Height:", MonitorHeight)
            break
else:
    print("No monitors detected.")

def get_monitor_dimensions():
    return MonitorWidth, MonitorHeight

def create_exp_screen():
    monitor_width, monitor_height = get_monitor_dimensions()
    expScreen = visual.Window(fullscr=False, color='grey', monitor='testMonitor', 
                              units='deg', size=(monitor_width, monitor_height))
    return expScreen

create_exp_screen()
