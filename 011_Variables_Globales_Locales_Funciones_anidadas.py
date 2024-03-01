#011_Variables_Globales_Locales_Funciones_anidadas

#Practica: 042_Variables_Globales_Locales_Funciones_anidadas
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

def funcion1(): #creamos una función
    global num1 #declaramos una variable global y le asignamos un valor
    num1 = 10

funcion1() #mandamos ejecutar la función

print(num1) #imprimimos el valor de la variable que ya fue asignado en la función y es global


def funcion1(): #creamos una función para anidar otra
    pass #dejamos vacia la función principal
    def funcion2(): #creamos la función anidada
        print('String en la función anidada.') #imprimimos un mensaje
    funcion2() #llamamos a la función anidada dentro de la función

funcion1() #llamamos a la función principal y muestra lo que escribimos en la anidada
