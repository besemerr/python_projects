import random
import time
from tkinter import *
import base64
from icon import img
import os

root = Tk()
root.title("Random Name Picker")
# root.iconbitmap('C:\\Users\\rbesemer\\PycharmProjects\\pythonProject\\RandomNamePicker\\images\\Icons8-Ios7-Gaming'
#                 '-Dice.ico')
tmp = open("temp.ico","wb+")
tmp.write(base64.b64decode(img))
tmp.close()
root.iconbitmap("temp.ico")
os.remove("temp.ico")
root.resizable(width=False, height=False)
root.configure(bg='black')


def build_list(*event):
    list_names = []
    num_names = int(textBox.index('end').split('.')[0])
    for i in range(1, num_names):
        name = textBox.get(str(i) + ".0", str(i) + ".0 lineend")
        if name != "":
            list_names.append(name)
    if len(list_names) != 0:
        winner = shuffle(list_names)
        outputLabel.config(fg='green', text=winner.upper())
    else:
        outputLabel2.config(text="ERROR: No names have been entered.")
        return


def animation(list_names):
    if len(list_names) == 10:
        max_rng = 2
    elif len(list_names) == 9:
        max_rng = 3
    elif len(list_names) == 8:
        max_rng = 4
    elif len(list_names) == 7:
        max_rng = 5
    elif len(list_names) == 6:
        max_rng = 6
    elif len(list_names) == 5:
        max_rng = 7
    elif len(list_names) == 4:
        max_rng = 8
    elif len(list_names) == 3:
        max_rng = 9
    elif len(list_names) == 2:
        max_rng = 10
    else:
        max_rng = 1
    for i in range(0, max_rng):
        for j in range(0, len(list_names)):
            outputLabel.config(fg='white', text=list_names[j].upper())
            root.update()
            time.sleep(.05)
            print(i)


def shuffle(list_names):
    number = random.randrange(0, 100000, 1)
    winner = ""
    counter = 0

    num_names = len(list_names) - 1
    for i in range(1, number):
        winner = list_names[counter]
        if counter == num_names:
            counter = 0
        else:
            counter += 1
    animation(list_names)
    outputLabel2.config(text="Looped through list of " + str(num_names + 1) + " names " + f"{number:,}" +
                             " times before \'" + winner + "\' was chosen.")
    return winner


def clear(event):
    if event.keysym == "BackSpace" or event.keysym == "Delete":
        outputLabel.config(fg='white', width=53, text="Enter all names in the field below, each on a separate line.",
                           font='Times\\New\\Roman 14 bold')
        outputLabel2.config(text='')
    elif event.keysym == "Escape":
        root.quit()


def button_focus(event):
    event.widget.tk_focusNext().focus()
    return "break"


root.bind("<Key>", clear)

outputLabel = Label(root, width=53, bg='black', fg='white', text="Enter all names in the field below, each on a "
                                                                 "separate line.", font='Times\\New\\Roman 14 bold')
outputLabel.pack(pady=5, ipady=5)

textBox = Text(root)
textBox.pack(padx=5)
textBox.bind("<Tab>", button_focus)

runButton = Button(root, width=53, bg='green', fg='white', command=build_list, text="Pick a Random Name",
                   font='Times\\New\\Roman 14 bold')
runButton.pack(pady=5)
runButton.bind("<Return>", build_list)

outputLabel2 = Label(root, text="", bg='black', fg='white')
outputLabel2.pack()

root.mainloop()

"""
Thomas Hipsher
Josue Ramos
Francisco Valdez
Starla Demeo
Toby Salcido
Ryan Besemer
Alex Blay-Borrow
"""