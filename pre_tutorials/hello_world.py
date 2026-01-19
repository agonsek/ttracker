# hello_world.py
# simple script to get to know PySimpleGUI

import PySimpleGUI as sg


sg.theme('DarkBlue')  # Add a touch of color

layout = [[sg.Text('Hello World!')], [sg.Button('OK')]]  # The layout of the window

window = sg.Window(title="Hello World", layout=layout, margins=(100, 50), relative_location=(350, 0))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()