#-------------------------------------------------------------------------------
# Name: gabriel gutierrez           ejercicio 3 opcion 2
#
# Author:      gabriel

# Created:     26/09/2022
# Copyright:   (c) aspro 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    correo = input("ngrese su email: ")
    if "@" in correo:
        print("Es válido")
    else:
        print("No es válido")

if __name__ == '__main__':
    main()
