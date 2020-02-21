#AVR_sumatoria.py
"""
Función que cree que solicite 10 valores de una lista y haga la sumatoria de los mismos e imprima
"""
class Sumatoria():
    suma = 0
    miLista = []
    def sumar(self):
        for i in range(0,10):
            dato = int(input("Ingrese el valor a guardar: "))
            self.miLista.append(dato)
            self.suma = self.suma + dato
        print("La sumatoria total es:",self.suma)
        
sumatoria = Sumatoria()
sumatoria.sumar()
