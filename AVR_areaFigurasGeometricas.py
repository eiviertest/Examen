def area_rectangulo(b,h):
        """Función calcula el área de rectángulo"""
        area = b*h
        print ("El area es: ",area)
 
def area_cuadrado(lado):
        """Función que calcula el área de un cuadrado"""
        area = lado**2
        print ("El area es: ",area)
 
 
def area_radio(radio):
        """Función que calcula el área de circulo, en base al radio"""
        pi = 3.1416
        area = radio**2*pi
        print ("El area es: ",area)
 
def area_diametro(diametro):
        """Función que calcula el área de circulo, en base al diametro"""
        pi = 3.1416
        radio = diametro / 2
        area = radio**2*pi
        print ("El area es: ",area)
 
def area_figura():
        """Función para decidir de que figura de desea obtener el área"""
        print ("Este programa de calcula area de 1==> 'circulo', 2==> 'cuadrado' y 3==> 'rectangulo'")
        figura = int(input("¿De qué figura deseas obtener área?: "))
        if figura == 1:
                area_circulo()
        elif figura == 2:
                lado = int(input("introduce el valor de un lado: "))
                area_cuadrado(lado)
        elif figura == 3:
                b = int(input("introduce el valor de la base: "))
                h = int(input("introduce el valor de la altura: "))
                area_rectangulo(b,h)
        else:
                print ("Introduzca un valor correcto, 'circulo', 'cuadrado' o rectángulo'")
 
def area_circulo():
        """Función si se elige la función area_figura() 'circulo', pasa a esta opcin, aquí se decide, si usar diametro o radio para obtener el área"""
        diametro_o_radio = int(input("¿Desea obtener area de circulo con 1==> 'radio' o 2==> 'diametro'?: "))
        if diametro_o_radio == 1:
                radio_1 = int(input("Introduce el valor del radio: "))
                area_radio(radio_1)
        elif diametro_o_radio == 2:
                diametro_1 = int(input("Introduce el valor del diametro: "))
                area_diametro(diametro_1)              
        else:
                print("Introduzca un valor correcto, 'radio' o 'diametro'")
 
while True:
        """Bucle principal del programa"""                     
        print ("Programa que calcula el área de figuras Geometrias")
        area_figura()
