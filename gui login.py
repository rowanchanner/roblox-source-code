import PySimpleGUI as sg
import time

        
        
    








sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('gui made by rowan channer')],
            [sg.Text('NOTE THIS WINDOW WILL STAY OPEN DONT CLOSE IT THANKYOU')],
            [sg.Text('please enter your username')],
            [sg.Text('username: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('N/A')] ]

# Create the Window
window = sg.Window('login', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'N/A': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])
    if event == 'Ok':
        import gui
        break
        


window.close()
