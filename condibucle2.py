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
    while opcion == 'suma', or 'resta', or 'multiplicacio':
        opcion=input("ingrese una opcion: ")
        continue
    if (opcion == "sumar"):
        print('opcion elegida: '+ op)
        resultado= num1+num2
        print(resultado)
    elif (opcion == "restar"):
        print('opcion elegida: '+ op)
        resultado1= num1-num2
        print(resultado1)
    elif (opcion == "multiplicacion"):
        print("multiplicar"+ op)
        resultado2= num1*num2
        print(resultado2)

    pass

if __name__ == '__main__':
    main()
