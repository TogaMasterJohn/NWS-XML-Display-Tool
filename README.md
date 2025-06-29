# NWS XML Display Tool

## version 0.9.1 by TogaMasterJohn/StormSpotterJohn

*This program is not affiliated with the National Oceanic and Atmospheric Administration or the National Weather Service – please do not contact them for support. If you have questions, please contact me on GitHub. Thank you!*

### Introduction

The National Weather Service XML Display Tool, or NWS XML Display Tool, is capable of importing and viewing most land current observation XML files from the National Weather Service. Users can also get links to useful pages on the National Weather Service’s website.

This program was created with Python version 3.6.9. The Linux version of IDLE 3.6.9 is/was used for development and testing.

### Required Modules

This program makes use of the following modules:

- Tkinter
- PIL
- xml.etree.ElementTree

### Supported Files

Currently, most land stations here in the continental U.S. are supported. Water stations are not supported at this time, and will not display anything. Support for water stations and land stations with different or missing XML tags are planned in a future release. Please see the “Future Release Plans” section for more information.

To download a ZIP file containing over 5,000 current observation XML files from the National Weather Service, visit https://forecast.weather.gov/xml/current_obs and select "All current XML files" (the ZIP file is usually ~5 MB; ~10 MB once extracted).

Direct link: https://forecast.weather.gov/xml/current_obs/all_xml.zip

### How to Use the Program

As of version 0.9.1:

There are three buttons in the main program window:

- Useful Links – opens the “Useful Links” window
- Open XML File – opens the “Open XML File” window�
- Exit – closes the program

##### Useful Links

Clicking this button will open a window that contains links to useful pages on the National Weather Service’s website. At this time, links are only visible.

##### Open XML File

Clicking this button will open an “Open XML File” window. Only XML files are allowed to be selected. Locate the current observation XML file that you wish to view and either double click on it or highlight it and select “Open.” From there, the program should display the appropriate contents of the current observation XML file in the program’s main window.

Note: it is highly recommended to close the program and relaunch the program in order to view another current observation XML file. A reset feature is planned for a future release. Please see the “Future Release Plans” section for more information.

##### Exit

Clicking this button will exit the program and close all windows associated with the program. Exiting the program and relaunching the program is highly recommended in order to view another current observation XML file.

### Future Release Plans

This version of the program is pretty much a proof-of-concept. This program was designed for a final project in a college class that I had to take. Due to time constraints, technical problems, development issues, and things going on in my personal life, some of the planned features could not be implemented before the due date. I do not wish to leave this program, or the concept of this program, behind. I would love to "finish" this program in the near future or design a program with the capabilities of this program and more!

The following features are planned for a future release, or in another program (with the same feature as this one):

- The ability to distinguish and view most, if not all, land and water stations
- A reset feature, so users can open and view more than just one current observation XML file at a time
- The ability to view NWS forecast XML files
- The ability to view a weather forecast office’s radar (via GIF)
- Calculators for wind chill, heat index, Fahrenheit to Celsius (and vice versa), MPH to knots (and vice versa), and other useful weather-related calculators
- Improve the GUI even further (more colors; make it look “fancier”)

### Contact

If you have any questions, comments, or suggestions, please contact me on GitHub. I will try to respond as soon as I can.

### Acknowledgments

I would like to thank my instructor, my classmates, my friends, and my family for their support, suggestions, and ideas. I could not have done this without you. And of course, I would like to thank the National Weather Service for their reliable forecasts and weather information.

###### 2022-2023 TogaMasterJohn/StormSpotterJohn
