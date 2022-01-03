
# el * delante del argumento de la funcion, quiere decir que recibe numero indeterminado de elementos
# y que esos elementos llegan en forma de tupla
def devuelve_ciudades(*ciudades):



    for elemento in ciudades:
        #for subElemento in elemento:
        # utilizar yield from es lo mismo que entrar con un for en el subElemento
            yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid","Barcelona","Monaco","Vilvao")


print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
