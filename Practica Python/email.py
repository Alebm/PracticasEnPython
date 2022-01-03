#practica para separa correos con .partition

email = str(input("Escriba el Email"))

parts = email.partition("@")


print("tu nombre de usuario es {}".format(parts[0]))
