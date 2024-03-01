#012_Importar_modulos_Funciones_lambda

#Practica: 043_Importar_modulos_Funciones_lambda
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

#import nombre_del_modulo //asi es como importamos modulos al programa

import math #importamos un modulo

def area(radio): #creamos la función area
	resultado = round(math.pi * radio * radio, 2) #calculamos el area usando el modulo math y redondeamos con round
	print(resultado) #imprimimos el resultado

area(2) #llamamos a la función introduciendo el radio del circulo


area = lambda radio: round(math.pi * radio * radio, 2) #esta es la forma de usar las funciones lambda que acortan el código

print(area(2)) #imprimimos la función con su radio
