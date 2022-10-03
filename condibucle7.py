#-------------------------------------------------------------------------------
# Name: condicional y bucles    ejercicio 7
#
# Author:      gabriel gutierrez
#
# Created:     02/10/2022
# Copyright:   (c) aspro 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

numb = [55, 4, 92, 1, 104, 64, 73, 99, 20]

value = None

for num in numb:
    if (value is None or num > value):
        value = num

print('Maximo value:', value)