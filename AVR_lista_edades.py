#AVR_lista_edades.py
#Funcion que cree un lista de 10 años de nacimiento e imprima las edades de todos los elementos
from random import randint
class Edades():
    miLista = []

    def edad(self):
        for i in range (0,10):
            numAzar = randint(1900,2019)
            self.miLista.append(numAzar)
        for elemento in self.miLista:
            print("La persona que nació en",elemento,"tiene ",(2020-elemento),"años")
            
edades = Edades()
edades.edad()
