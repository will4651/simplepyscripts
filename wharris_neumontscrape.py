#Script setup
import PySimpleGUI as sg
import wharris_scraper

#Define window content
layout = [
    [sg.Column(
        [[sg.Text('Click the scrape button to recieve the current Adademic Calendar\nfor Neumont College of Computer Science!', key = 'display')]], size = (400, 400), scrollable = True,  vertical_scroll_only = True, key = 'column')
    ],
    [sg.Button('Scrape', bind_return_key = True), sg.Button('Quit')]
]

#Create the window
window = sg.Window('Getting into a Scrape at Neumont', layout)

#Main program loop
while True:
    #Display window
    event, values = window.read()

    #Check if user pressed quit or if window was closed, also run code when scrape button is clicked
    if (event == sg.WINDOW_CLOSED) or (event == 'Quit'):
        break
    elif (event == 'Scrape'):
        window['display'].update(wharris_scraper.scrape())
        window.refresh()
        window['column'].contents_changed()

#Close window after main loop is broken out of
window.close()