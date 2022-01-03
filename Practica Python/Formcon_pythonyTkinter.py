import tkinter as tk
from tkinter.constants import END, X
from typing import Text

def send_data():

# tomamos los datos con un get de los entrys
    username_data = username.get()
    password_data = password.get()
    fullname_data = fullname.get()
    age_data      = age.get()

    print(username_data,"\n",password_data,"\n",fullname_data,"\n",age_data)

# registramos los datos en un txt, con espacion "\t", y un salto de linea al fina "\n"
   
    registro = open("Registros.txt","a")
    registro.write(username_data)
    registro.write("\t")
    registro.write(password_data)
    registro.write("\t")
    registro.write(fullname_data)
    registro.write("\t")
    registro.write(age_data)
    registro.write("\n")
    registro.close()
    
   

    # sirve para borrar los campos de datos desde el index 0 hasta el final

    username_entry.delete(0,END)
    password_entry.delete(0,END)
    fullname_entry.delete(0,END)
    age_entry.delete(0,END)



window = tk.Tk()
window.geometry("600x600")
window.title("Formulario python y tkinter")

window.config(background="gray")


usesname_labe = tk.Label(text="username")
usesname_labe.place(x= 22, y= 70)
password_labe = tk.Label(text="Password")
password_labe.place(x= 22, y= 130)
fullname_labe = tk.Label(text="fullname")
fullname_labe.place(x= 22, y= 190)
age_label = tk.Label(text="age")
age_label.place(x= 22, y= 250)

username = tk.StringVar()
password = tk.StringVar()
fullname = tk.StringVar()
age      = tk.StringVar()

username_entry = tk.Entry(textvariable=username, width="40")
username_entry.place(x=22, y= 100)
password_entry = tk.Entry(textvariable=password, width="40", show="*")
password_entry.place(x=22, y= 160)
fullname_entry = tk.Entry(textvariable=fullname, width="40")
fullname_entry.place(x=22, y= 220)
age_entry      = tk.Entry(textvariable=age, width="40")
age_entry.place(x=22, y= 280)


submit_btn = tk.Button(window, text="Submit info", command=send_data, width="30", height="2")
submit_btn.place(x=22,y=320)




window.mainloop()