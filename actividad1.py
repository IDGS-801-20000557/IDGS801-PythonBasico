#le pide un numero y le imprime la tabla de multiplicar del 1 al 10

print("valores de usuario")

num1=int(input('Dame valor: '))


for n in range(1,11):
    print("{}*{}={}".format(num1,n,(num1*n)))

