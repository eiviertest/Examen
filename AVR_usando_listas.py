#AVR_usando_listas.py

class Lista():

    def hacerLista(self):
        miLista = []
        respuesta = 1 #Agregar legumbre
        while respuesta==1:
            entrada = input("Ingrese la legumbre a guardar: ")
            miLista.append(entrada)
            respuesta = int(input("¿Quiere guardar otra legumbre? \n 1==> 'Si' \n 2==> 'No' \n Respuesta: "))
                 
        siImprimir = int(input("¿Desea imprimir la lista? \n 1==> 'Si' \n 2==> 'No' \n Respuesta: "))    
        if siImprimir == 1:
            print("Usted necesita comprar==> ")
            for elemento in miLista:
                print(elemento)

lista = Lista()
lista.hacerLista()
