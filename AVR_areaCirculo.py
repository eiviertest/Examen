#AVR_areaCirculo.py
from math import pi
class AreaCirculo():

    def areaRadio(self, radio):
        area = pi*self.radio**2
        print ("El área es: ",area)

    def areaDiametro(self, diametro):
        area = pi*(self.diametro/2)**2
        print ("El area es: ",area)

areaCirculo = AreaCirculo()
while True:
    respuesta = int(input("Calcular el área del circulo por: \n 1==> 'Radio' \n 2==> 'Diametro' \n Respuesta: "))
    if respuesta == 1:
        radio = float(input("Ingrese el radio: "))
        areaCirculo.areaRadio(radio)
    else:
        diametro = float(input("Ingrese el diametro: "))
        areaCirculo.areaDiametro(diametro)
