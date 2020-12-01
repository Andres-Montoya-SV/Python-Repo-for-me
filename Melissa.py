# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 01:41:12 2020

@author: ricardo.montoya
"""

from tkinter import *
import pyttsx3

root = Tk()
root.title("Trail")
root.geometry("800x500")

def talk():
    engine = pyttsx3.init()
    engine.setProperty('rate', 190)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',  voices[1].id)
    engine.say(my_entry.get())
    engine.save_to_file(my_entry.get(), 'test.wav')
    engine.runAndWait()
    my_entry.delete(0, END)

my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack(pady=20)

my_button = Button(root, text = "Speak", command = talk)
my_button.pack(pady=20)

root.mainloop()