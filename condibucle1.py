#-------------------------------------------------------------------------------
# Name: gabriel gutierrez    ejercicio 1
#
# Author:      gabriel
#
# Created:     26/09/2022
# Copyright:   (c) aspro 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("verifica si es numero impar")
    contador=0
    while True:
        numero=int(input("ingrese un numero impar: "))
        contador=contador+1
        if numero %2:
            print("es numero impar ")
            break
        print("es numero part ")

    pass

if __name__ == '__main__':
    main()
