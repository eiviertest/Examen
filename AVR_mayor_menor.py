#AVR_mayor_menor.py
class MayorMenor():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def numeroMayor(self):
        if num1<num2:
            return num2
        else:
            return num1

    def numeroMenor(self):
        if num1>num2:
            return num2
        else:
            return num1

num1 = float(input('Ingrese primer número: '))
num2 = float(input('ingrese segundo número: '))
mayorMenor = MayorMenor(num1, num2)
print("El número mayor es:", mayorMenor.numeroMayor())
print("El número menor es:", mayorMenor.numeroMenor())
