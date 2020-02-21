#AVR_areaCirculo.py
from math import pi
class AreaCirculo():

    def area(self):
            respuesta = int(input("Calcular el área del circulo por: \n 1==> 'Radio' \n 2==> 'Diametro' \n Respuesta: "))
            if respuesta == 1:
                radio = float(input("Ingrese el radio: "))
                return pi*radio**2
            else:
                diametro = float(input("Ingrese el diametro: "))
                return pi*(diametro/2)**2
        
areaCirculo = AreaCirculo()
print("El área del circulo es:",areaCirculo.area(), "unidades cuadradas")
