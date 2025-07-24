#Script setup
import PySimpleGUI as sg
import textwrap
import wharris_heavylifter
from urllib.request import urlopen
from urllib.request import Request

def main():
    #Define window content
    sg.theme('BlueMono')
    imageColumn = [sg.Image(key = 'imagedisplay', size = (40, 40))], [sg.Text('Enter a valid URL and click the scrape button to receive a list of\nimages found!', key = 'textdisplay')]
    textColumn = [[sg.Listbox([], key = 'display', enable_events = True, horizontal_scroll = True, size = (60, 20))], [sg.Input(key = 'input'), sg.Button('Scrape', key = 'scrape', bind_return_key = True), sg.Button('Quit')]]

    layout = [
        [sg.Column(textColumn), sg.Column(imageColumn)]
    ]

    #Create the window
    window = sg.Window('I Get The Picture', layout)

    #Main program loop
    while True:
        #Display window
        event, values = window.read()

        #Check if user pressed quit or if window was closed, run code when scrape button is clicked, and run code when item from listbox is selected
        if (event == sg.WINDOW_CLOSED) or (event == 'Quit'):
            break
        elif (event == 'scrape'):
            data = wharris_heavylifter.scrape(values['input'])
            window['display'].update(data)
            window.refresh()
        elif (event == 'display'):
            url = str(window['display'].get()[0])
            window['textdisplay'].update(textwrap.fill(url, 65))
            try:
                req = Request(str(url), headers={'User-Agent' : "Browser"})
                src = urlopen(req).read()
                window['imagedisplay'].update(src)
            except:
                window['textdisplay'].update('Something went wrong trying to grab the image!')

    #Close window after main loop is broken out of
    window.close()

if __name__ == "__main__":
    main()