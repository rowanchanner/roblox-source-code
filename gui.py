import PySimpleGUI as sg
import pyautogui
import keyboard
import webbrowser

sg.theme('BrightColors')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('wlecome to the gui it is still in devlopment so please be kindand send me any ides you have!')],
            [sg.Button('auto clicker')],
            [sg.Button('Scource Code!'), sg.Button('close')] ] 

# Create the Window
window = sg.Window('rowans GUI', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'auto clicker':
        while True:
            if keyboard.is_pressed("q"):
                count = 0
                while count < 5:
                    pyautogui.click()
                    pyautogui.click()
                print("q pressed, ending loop")
                break

            
    if event == 'Source Code':
        webbrowser.open_new()

    if event == sg.WIN_CLOSED or event == 'close' :
        break

window.close()
