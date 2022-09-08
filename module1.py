#-------------------------------------------------------------------------------
# Name: gabriel angel gutierrez fernandez       module1
#
# Author:      gabriel
#
# Created:     07/09/2022
# Copyright:   (c) gabriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    if True:
        b = 50
        a = 2
        # division de b y a
        c = b // a
        # potencia de b^a
        d = b**a
        print(f"el total es {c}")
        print(f"el total de la potencia es {d}")
        # salto de linea
    print("mision completa")
    #imprimir por pantalla un salto de linea
    print(" ")
    name = "gabriel"
    age = 23
    # la variable "  "es para separar la cadena de variables
    espacio = " "
    apellido = "gutierrez"
    DNI = input("ingrese su DNI ")
    cadena = name + espacio + apellido
    print(f"{cadena} de {age} años")
    print(f"y su DNI es {DNI}")


if __name__ == '__main__':
    main()
