"""Este algoritmo le ayuda a saber la longitud de una cadena de texto"""
class LongitudCadena():

    def __init__(self, txt):
        self.txt = txt

    def longitud(self):
        return len(self.txt)

print("Programa para saber la longitud de una cadena")
cadena = input("Ingrese el texto para calcular la cantidad de carácteres: \n")
longitudCadena = LongitudCadena(cadena)
print("El texto que usted ingresó contiene",longitudCadena.longitud(), "carácteres")

