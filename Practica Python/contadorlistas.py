
frase = str(input("ingresa una frase: "))

fraseCortada = frase.split(" ")
contador_palabras = {}
contador = 0



for i  in range (0,len(fraseCortada)):
    primerapalabra = fraseCortada[i]
    #print(primerapalabra)
    for k in range(0, len(fraseCortada)):
        segundapalabra = fraseCortada[k]
            #print("segunda P:", segundapalabra)
        if primerapalabra == segundapalabra:
            contador +=1
    contador_palabras[primerapalabra] = contador
    contador = 0



print(contador_palabras)    

