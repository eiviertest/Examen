#AVR_areaTriangulo.py

class AreaTriangulo():

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base) * (self.altura) / 2.0

print ("Calcular el área de un triángulo")
base= float(input("¿Cuál es la base? "))
altura= float(input("¿Cuál es la altura? "))
areaTriangulo = AreaTriangulo(base, altura)
print("El área del triágulo es:", areaTriangulo.area(), "unidades cuadradas")
