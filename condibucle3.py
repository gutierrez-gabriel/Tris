#-------------------------------------------------------------------------------
# Name: gabriel gutierrez       ejercicio 3
#
# Author:      gabriel
#
# Created:     26/09/2022
# Copyright:   (c) aspro 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    valido= False
    email=input('ingresa tu emal: ')
    for i in range(len(email)):
        if email [i]=='@':
            valido= True
    if valido:
        print('email es correcto')
    else:
        print('email esincorrecto')
    pass

if __name__ == '__main__':
    main()
