import PySimpleGUI as sg
import json as json

#Setting up necessary variables and messages
startText = """
Data is stored in the following format:
First Name
Last Name
Phone

Commands:
list: Lists all stored entries
find [value]: Finds first entry that has matching
value
add [fname] [lname] [phone]: Adds entry with
listed values
del [value]: Deletes first entry that has matching
value
quit: Quits program"""
knownCommandText = "Command Recognized: {}"
unknownCommandText = "Command Not Recognized: {}"
readData = []
updateData = []

#Create db.json if doesn't exist
def createDB():
    try:
        with open('db.json', 'w') as f:
            json.dump([], f)
    except:
        print("createDB() failed")
    else:
        print("createDB() successful")

#Reads and parses db.json
def readDB():
    global readData
    global updateData
    try:
        with open('db.json', 'r') as f:
            global readData
            readData = json.loads(f.read())
            updateData = readData
            #print(readData)
    except:
        print('readDB() failed')
    else:
        print("readDB() successful")

#Append to data and write to db.json
def appendDB(fname, lname, phone):
    global readData
    global updateData
    try:
        updateData = readData
        updateData.append({
            'fname': str(fname),
            'lname': str(lname),
            'phone': str(phone)
        })
        with open('db.json', 'w') as f:
            json.dump(updateData, f)
    except:
        print("appendDB() failed")
    else:
        print("appendDB() successful")

#Write data to db.json
def writeDB():
    global updateData
    try:
        with open('db.json', 'w') as f:
            json.dump(updateData, f)
    except:
        print("writeDB() failed")
    else:
        print("writeDB() successful")

#Update display text and scrollable area
def updateColumn(t):
    window['display'].update(t)
    window.refresh()
    window['column'].contents_changed()

#Iterate through db.json, assemble list text, and update window with list text
def list():
    global readData
    print("listing db...")
    t = ''
    readDB()
    for count, item in enumerate(readData, 1):
        t += 'Index ' + str(count-1) + ':\n'
        t += 'First Name: ' + item['fname'] + '\n'
        t += 'Last Name: ' + item['lname'] + '\n'
        t += 'Phone: ' + item['phone'] + '\n\n'
    updateColumn(t)
    print("listing finished")

#Iterate through db.json, and update display text with first matching result
def find(i):
    global readData
    print("finding value...")
    t = ''
    readDB()
    for count, item in enumerate(readData, 1):
        if (str(item['fname']).lower().rfind(str(i).lower()) > -1) or (str(item['lname']).lower().rfind(str(i).lower()) > -1) or (str(item['phone']).lower().rfind(str(i).lower()) > -1):
            t = 'Value found at index ' + str(count - 1) + ':\n'
            t += 'First Name: ' + item['fname'] + '\n'
            t += 'Last Name: ' + item['lname'] + '\n'
            t += 'Phone: ' + item['phone']
            break
        else:
            t = "No entry found"
    updateColumn(t)
    print("finding finished")

#Add item to data, then write to db.json
def add(fname, lname, phone):
    print("adding value...")
    readDB()
    appendDB(fname, lname, phone)
    t = 'Value added at index ' + str(len(readData)-1) + ':\n'
    t += 'First Name: ' + fname + '\n'
    t += 'Last Name: ' + lname + '\n'
    t += 'Phone: ' + phone
    updateColumn(t)
    print("adding finished")

#Iterates through db.json, removes matching item from data, and writes to db.json
def delete(i):
    global readData
    global updateData
    t = ''
    print("deleting value...")
    readDB()
    for count, item in enumerate(readData, 1):
        if (str(item['fname']).lower().rfind(str(i).lower()) > -1) or (str(item['lname']).lower().rfind(str(i).lower()) > -1) or (str(item['phone']).lower().rfind(str(i).lower()) > -1):
            updateData.pop(count-1)
            t = 'Value deleted at index ' + str(count-1) + ':\n'
            t += 'First Name: ' + item['fname'] + '\n'
            t += 'Last Name: ' + item['lname'] + '\n'
            t += 'Phone: ' + item['phone']
            break
        else:
            t = "Value not found"
    writeDB()
    updateColumn(t)
    print("deleting finished")

#Define window content
layout = [
    [sg.Column([[sg.Text(startText, key = 'display')]], size = (300, 400), scrollable = True,  vertical_scroll_only = True, key = 'column')],
    [sg.Input(key = 'input')],
    [sg.Text(size = (40, 1), key = 'output')],
    [sg.Button('Ok', key = 'submit', bind_return_key = True), sg.Button('Quit')]
]

#Initial db setup
#Attempts to read db.json and creates db.json if it doesn't exist
try:
    readDB()
except:
    print("db.json doesn't exist, creating")
    createDB()
    readDB()
    print("db.json created, read successful")
else:
    print("db.json exists, read successful")

#Create the window
window = sg.Window('Data at Your Command', layout)

#Main program loop
while True:
    #Display window
    event, values = window.read()

    #Check if user pressed quit or if window was closed
    if (event == sg.WINDOW_CLOSED) or (event == 'Quit'):
        break

    #Save user input to variable, if none set to empty string
    try:
        cmd = str(values['input']).split()[0]
    except:
        cmd = ''

    #Code for command recognition
    #If command and syntax is correct, show recognition text
    #If syntax is incorrect, show correct syntax
    #If input matches no known commands, show unrecognized command text
    match cmd:
        case "list":
            window['output'].update(knownCommandText.format(cmd))
            list()
        case "find":
            if len(str(values['input']).split()) == 2:
                window['output'].update(knownCommandText.format(cmd))
                find(str(values['input']).split()[1])
            else:
                window['output'].update("Correct syntax for find: find [value]")
        case "add":
            if len(str(values['input']).split()) == 4:
                window['output'].update(knownCommandText.format(cmd))
                add(str(values['input']).split()[1], str(values['input']).split()[2], str(values['input']).split()[3])
            else:
                window['output'].update("Correct syntax for add: add [fname] [lname] [phone]")
        case "del":
            if len(str(values['input']).split()) == 2:
                window['output'].update(knownCommandText.format(cmd))
                delete(str(values['input']).split()[1])
            else:
                window['output'].update("Correct syntax for del: del [value]")
        case "quit":
            window.close()
            print("quit successful")
        case _:
            window['output'].update(unknownCommandText.format(cmd))

#Close window after main loop is broken out of
window.close()