import tkinter as tk

import random
from typing import Text

#codigo para el cambio de color

def changedcolor():
    colors= ["#FF5733","#B46352","#41C951","#49764F"]
    random_colors = random.choice(colors)
    mywindow.config(background=random_colors)

mywindow = tk.Tk()
mywindow.geometry("600x600")
mywindow.resizable(False,False)
mywindow.title("Cambio de color de la ventana con un boton")

main_title = tk.Label(text="python+tkinter",font=("Tahoma,12"),bg="white",fg="black",width=70,height=4)
main_title.place(x=0,y=10)

#boton para cambio de color

main_btn = tk.Button(mywindow, text="cambio de color", command=changedcolor)
main_btn.place(x=60,y=60 )


mywindow.mainloop()