import os
class OperasBas:
    #definimos propiedades de clases
    n1=0
    n2=0
    res=0

    #definimos constructor de clase
    def __init__(self, a, b):
        self.n1=a
        self.n2=b

    #metodos de clase
    def suma(self):
        self.res=self.n1+self.n2

    def resta(self):
        self.res=self.n1-self.n2
    
    def multiplicacion(self):
        self.res=self.n1*self.n2

    def division(self):
        self.res=self.n1/self.n2    

def main():
    i=0
   
    while i != 5:
        print('------------------------------')
        print("valores de la operación:")
        num1=int(input('Dame valor 1: '))
        num2=int(input('Dame valor 2: '))
        obj=OperasBas(num1,num2)
        print("Escribe <1> para sumar")
        print("Escribe <2> para restar")
        print("Escribe <3> para multiplicar")
        print("Escribe <4> para dividir")
        print("Escribe <5> para salir")
        i=int(input())
        os.system ("cls") 
        match i:
            case 1:
                 obj.suma()
                 
                 print("La suma es: {}".format(obj.res))
            case 2:
                 obj.resta()
                 print("La resta es: {}".format(obj.res))
            case 3:
                 obj.multiplicacion()
                 print("La multiplicacion es: {}".format(obj.res))
            case 4:
                 obj.division()
                 print("La division es: {}".format(obj.res))



   

if __name__== '__main__':
    main()