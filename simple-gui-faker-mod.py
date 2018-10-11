"""

Shout out PySimpleGUI
Program to display fake data from Faker
Education purposes 

"""
import sys
import time
import faker
from faker import Faker
from time import sleep


def SecondForm():
    """ This window opens up when PROPERTIES is pressed """
    import PySimpleGUI as sg

    layout = [[sg.Text(' \n')],
              [sg.OK()]]

    window = sg.Window('JDG').Layout(layout)
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
    sg.SetOptions(element_padding=(10, 0))

    # ------ Menu Definition ------ #
    menu_def = [['&File', ['&Open', '&Save', '---', 'Properties', 'E&xit' ]],
                ['&Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                [''
                 '&Help', '&About...'],]

    # ------ GUI Definition ------ #
    layout = [
            [sg.Menu(menu_def, tearoff=True)],
            [sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3', FakeGenerator()], size=(60, 30), background_color="white")],
            [sg.In('JDG', size=(10,10))]
        ]

    window = sg.Window("PySimpleGUI W/ Faker Module", default_element_size=(12, 1), auto_size_text=False, auto_size_buttons=False,
                       default_button_element_size=(12, 1)).Layout(layout)


    # ------ Loop & Process button menu choices ------ #
    while True:
        button, values = window.Read()
        if button is None or button == 'Exit':
            return
        print('Button = ', button)
        # ------ Process menu choices ------ #
        if button == 'About...':
            window.Hide()
            sg.Popup('About...','Version 1.0', 'JDG', '2018', grab_anywhere=True)
            window.UnHide()
        elif button == 'Open':
            filename = sg.PopupGetFile('file to open', no_window=True)
            print("File Selected = ", filename)
        elif button == 'Properties':
            SecondForm()



TestMenus()
