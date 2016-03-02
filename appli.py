#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
fenetre = Tk()

def oneself():
    error = 0
    the_lastname = lastname_input.get().strip()
    the_firstname = firstname_input.get().strip()
    the_age = age_input.get().strip()
    if the_lastname == "":
        error = error + 1
        messagebox.showwarning("Lastname", "Your lastname can't be empty !!")
    if the_firstname == "":
        error = error + 1
        messagebox.showwarning("Firstname", "Your firstname can't be empty !!")
    if the_age.isdigit() == False:
        error = error + 1
        messagebox.showwarning("Age", "Your age must be an integer !!")

    if error == 0:
        messagebox.showinfo("Yay !!", "Hello {0} {1} !! You're {2} years old !!".format(the_lastname, the_firstname, the_age))


lastname_label = Label(fenetre, text = "Your lastname ?")
lastname_label.pack()

lastname = StringVar()
lastname_input = Entry(fenetre, textvariable = lastname, width = 30)
lastname_input.pack()

firstname_label = Label(fenetre, text = "Your firstname ?")
firstname_label.pack()

firstname = StringVar()
firstname_input = Entry(fenetre, textvariable = firstname, width = 30)
firstname_input.pack()

age_label = Label(fenetre, text = "How old are you ?")
age_label.pack()

age_input = Spinbox(fenetre, from_ = 1, to = 150)
age_input.pack()

validate_button = Button(fenetre, text = "Send", command = oneself)
validate_button.pack()

quit_button = Button(fenetre, text = "Quit", command = fenetre.quit)
quit_button.pack()

fenetre.mainloop()