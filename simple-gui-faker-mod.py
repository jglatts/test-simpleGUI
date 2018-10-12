"""

Shout out PySimpleGUI
Program to display fake data from Faker
Education purposes 

"""
import sys
import time
import psutil
import faker
from faker import Faker
from time import sleep


def SecondForm():
    """ This window opens up when PROPERTIES is pressed """
    import PySimpleGUI as sg

    print("\n\n Viewing Properties \n\n")  # printed in the console, not the GUI
    cpu_freq = psutil.cpu_freq()
    cpu_count = psutil.cpu_count()

    string_freq = str(cpu_freq)  
    string_count = str(cpu_count)

    layout = [[sg.Text(string_freq)],
              [sg.Text(string_count)],
              [sg.OK()]]

    window = sg.Window('CPU PROPERTIES').Layout(layout)
    b, v = window.Read()


def FakeGenerator():
    """ Generate random names to be displayed """
    i = 0
    name_list = []
    while i < 10:
        fake = Faker()
        random = fake.name()
        name_list.append(random)
        name_list.append("--")
        i += 1

    #for name in name_list:
    #   return name
    return name_list


def TestMenus():
    import PySimpleGUI as sg

    sg.ChangeLookAndFeel('BluePurple')
    sg.SetOptions(element_padding=(4, 4))

    """ Menu Definition """
    menu_def = [
                    ['&File', ['&Open', '&Save', '---', 'CPU Properties']],
                    ['&Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                    ['' '&Help', '&About...'],
                    ['&Exit', ['&Hmm..']]
                ]


    """ GUI Definition """
    layout = [
                [sg.Menu(menu_def, tearoff=True)],
                [sg.Listbox(values=[FakeGenerator(), FakeGenerator(), FakeGenerator(), FakeGenerator()], size=(40, 10), background_color="white")],
                [sg.In('JDG', size=(50,10))]
            ]

    window = sg.Window("PySimpleGUI W/ Faker Module", default_element_size=(14, 1), auto_size_text=False, auto_size_buttons=False,
                       default_button_element_size=(14, 1)).Layout(layout)


    """ Loop & Process button menu choices """
    while True:
        button, values = window.Read()
        if button is None or button == 'Exit':
            return
        print('Button = ', button)
        """ Process menu choices """ 
        if button == 'About...':
            window.Hide()
            sg.Popup('About...','Version 1.0', 'JDG', '2018', grab_anywhere=True)
            window.UnHide()
        elif button == 'Open':
            filename = sg.PopupGetFile('file to open', no_window=True)
            print("File Selected = ", filename)
        elif button == 'CPU Properties':
            SecondForm()
        elif button == 'Hmm..':
            return



TestMenus()
