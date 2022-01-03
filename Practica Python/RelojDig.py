import tkinter as tk
from time import strftime
from tkinter import font

root = tk.Tk()
root.title("Reloj Digital Tkinter en Python")


reloj = tk.Label()
reloj['text'] = '21:18:00'
reloj.pack() 
reloj['font'] = 'DS-Digital 150 bold'


strftime('%H:%M:%S')

def tic():
    reloj['text'] = strftime('%H:%M:%S')

tic()

def tac():
    tic()
    reloj.after(1000, tac)

tac()


root.mainloop()