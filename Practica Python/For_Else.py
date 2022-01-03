
email= input(" Introduce un email ")

contador=0


for i in email:

    if i=="@":

        contador+=1
        arroba = True

        break

else:

    arroba=False

print(arroba)
print(contador)