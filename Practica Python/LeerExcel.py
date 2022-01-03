#leer datos desde excel con pandas y openpyxl


import pandas as pd

Ruta = r'C:\Users\Bedoy\Documents\datos.xlsx'

data = pd.read_excel(Ruta)
#print(data)
print(data.__str__())

get_email = data.get('Email')

list_email = list(get_email)


print(list_email)
print(get_email)

with open("emails_data.txt", "w") as f:
    for item in list_email:
        f.write(item + "\n")    


# metodo normal para escribir en el archivo sin usar el with

f = open("emails_data2.txt","w")
for item in list_email:
    f.write(item + "\n")

    
f.close