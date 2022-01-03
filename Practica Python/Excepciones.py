def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicacion(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

op1=(int(input(" primer numero: ")))

op2=(int(input(" segundo numero: ")))


operacion=input( "introduce la operacion  (suma,resta,multiplicacion,division): ")


if operacion=="suma":
    print(suma(op1,op2))

elif operacion=="resta":
    print(resta(op1,op2))

elif operacion=="multiplicacion":
    print(multiplicacion(op1,op2))

elif operacion=="division":
    print(division(op1,op2))

else:
    print("Operacion no existe")
