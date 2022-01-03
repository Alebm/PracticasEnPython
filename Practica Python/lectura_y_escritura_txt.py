#Leer la data del archivo "data.txt" y sacar usuario y password del archivo, creando otros txt respectivos par acada item

from os import close


f = open("data.txt",'r')
username = open("user.txt",'w')
password = open("pass.txt",'w')


for i in f:
    parts = i.split(':')
    name = parts[3]
    single_pass = parts[4]
    username.write(name)
    username.write('\n')
    password.write(single_pass)
    password.write('\n')

f.close
username.close
password.close
