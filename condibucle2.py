#-------------------------------------------------------------------------------
# Name: gabriel gutierrez      ejercicio 2
#
# Author:      gabriel
#
# Created:     26/09/2022
# Copyright:   (c) aspro 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    num1=int(input("ingrese un numero: "))
    num2=int(input("ingrese otro numero: "))
    print("sumar, restar, multiplicar")
    opcion=input("ingrese una opcion: ")

    while (opcion != 'sumar') and (opcion != 'restar') and (opcion != 'multiplicar') :
        opcion=input("ingrese una opcion: ")

    if (opcion == "sumar"):
        print('opcion elegida: '+ opcion)
        resultado= num1+num2
        print(resultado)
    elif (opcion == "restar"):
        print('opcion elegida: '+ opcion)
        resultado1= num1-num2
        print(resultado1)
    elif (opcion == "multiplicar"):
        print('opcion elegida: '+ opcion)
        resultado2= num1*num2
        print(resultado2)

    pass

if __name__ == '__main__':
    main()
