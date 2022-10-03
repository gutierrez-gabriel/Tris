#-------------------------------------------------------------------------------
# Name: gabriel gutierrez       ejercicio 3 opcion 3
#
# Author:      gabriel
#
# Created:     26/09/2022
# Copyright:   (c) aspro 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re

def validar(valor):
	patron_email = '^\w(\w|\.)*@\w(\w|\.)*\.\w\w+$'
	resultado = re.search(patron_email, valor)
	return resultado


valido = False

print('Introduzca una dirección de correo electrónico: ', end='')

while not valido:
	valor = input()
	valido = validar(valor)
	if not valido:
		print('Lo siento, la dirección no es válida, vuelva a intentarlo: ', end='')

print(f'El valor válido es {valor}.')