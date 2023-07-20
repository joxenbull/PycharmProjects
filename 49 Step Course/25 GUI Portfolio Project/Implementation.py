# In parts
# create menu and layout
# Fonts - Current
# Font - Change the type and sizes
# Display about
# Close
# Save
# Save As
# first time save
# Open

import PySimpleGUI as sg

# to save
import io

# for directory
import os
scriptPath = os.path.dirname(__file__)

# Fonts
currentSize = 12
currentFont = 'Arial'

# About
def about():
    sg.popup('About this program, Version 1.0 Beta, Elite Text Editor, Copyright @2023')

# first Time Save
firstTimeApp = 1

# save
# name, write mode and encode
# use the filename instead of data.txt, make filename global
def save(data):
    if filename != '':

        # with io.open('data.txt', 'w', encoding = 'utf8') as f:
        with io.open(filename, 'w', encoding='utf8') as f:
            f.write(data)

# Save as
# the type
# the where
# global file name declaration
def save_as(data):
    global filename
    filename = sg.tk.filedialog.asksaveasfilename(
        defaultextension = 'txt',
        filetypes = (('ALL TXT FILES,','*.txt'),('All Files','*.*')),
        initialdir = scriptPath,
        title = 'Save As')

    if filename != '':
        with io.open(filename, 'w', encoding='utf8') as f:
            f.write(data)

# Open
# call it, open and update to
def open_file():
    # no window... is from Tkinter and looks better
    fileopen = sg.popup_get_file('file to open', no_window=True)

    # if cancel without select file then no issue
    if fileopen != '':
        with open(fileopen, 'r', encoding='utf8') as f:
            text = f.read()
        window['_text'].update(value = text)
        window.TKroot.title(fileopen)

# MENU
menu = [
        ['File', ['Open', 'Save', 'Save As', 'Close']],
        ['Edit', ['Font',['Arial', 'Courier'], ['Size', ['8','12','16','20']]]],
        ['About', ['Version']]
       ]

# layout
layout = [
            [sg.Menu(menu)],
            [sg.Multiline(size = (400,60),font=('Arial',12), key = '_text')]
          ]

window = sg.Window('Elite Text Editor', layout, resizable = True, size=(800,600), icon = 'favicon.ico')

# infinite lop
while True:
    event, values = window.read()

    # close
    if event == sg.WIN_CLOSED or event == 'Close' :
        break

# change font type
    if event == 'Courier':
        currentFont = 'Courier'
        font = ('Courier', currentSize)
        window['_text'].update(font=font)

    if event == 'Arial':
        currentFont = 'Arial'
        font = ('Arial', currentSize)
        window['_text'].update(font=font)

# change font size
    if event == '8':
        currentSize = '8'
        font = (currentFont, '8')
        window['_text'].update(font = font)

    if event == '12':
        currentSize = '12'
        font = (currentFont, '12')
        window['_text'].update(font = font)

    if event == '16':
        currentSize = '16'
        font = (currentFont, '16')
        window['_text'].update(font = font)

    if event == '20':
        currentSize = '20'
        font = (currentFont, '20')
        window['_text'].update(font = font)

# about version
    if event == 'Version':
        about()

# save
    # check if it is first time
    # if fist time require to input the name
    # else continues to update
    if event == 'Save':
        if firstTimeApp == 0:
            save(values['_text'])
        else:
            save_as(values['_text'])
            firstTimeApp = 0

# save As
    if event == 'Save As':
        save_as(values['_text'])

# Open
    if event == 'Open':
        open_file()

window.closed()