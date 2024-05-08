# Psychopy-Coder
Here I provide some fun and useful codes for Psychopy Coder, note that they can be used also in Builder, but total focus is on Coder

#Screen.py
This code is designed to detect the number of monitors connected to the system and create a window on the primary monitor.
The code uses the screeninfo library to detect the number of monitors and their dimensions. 
If a single monitor is detected, the code uses the dimensions of that monitor to create a window. 
If multiple monitors are detected, the code uses the dimensions of the primary monitor to create a window.

The code uses screeninfo library, if you dont have it install first, using the following command:
pip install screeninfo
NOTE: code is tested with Psychopy 2023.x.x versions.
