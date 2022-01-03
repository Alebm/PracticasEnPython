def generaPares(limite):

    num=1

   
    while num<limite:

        yield num*2    

        num=num+1

devuelvePares=generaPares(10)

#genera el primer numero par
print(next(devuelvePares))

# un stand by y luego genera el otro numero par
print("Aqui podria ir mas codigo")

# genera el otro numero par
print(next(devuelvePares))

#nuevo stand by .... etc
print("Aqui podria ir mas codigo")
