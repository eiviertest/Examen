from random import randint

class MenorMayor():
 
    def mayorMenor(self):
        numLimite = int(input("¿Cúal es el número límite para generar un número aleatorio(solamente enteros): "))
        numAzar = randint(0,numLimite)
        numero = float(input('Ingrese el número a comparar: '))
        if numAzar>numero:
            print('El número mayor es el generado, que es: ', numAzar)
        else:
            print('El número mayor es el ingresado, que es:' , numero)
            
numMenorMayor = MenorMayor()
numMenorMayor.mayorMenor()
