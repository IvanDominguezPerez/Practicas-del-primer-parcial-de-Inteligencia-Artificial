#009_Funciones

#Practica: 033_Funciones_Creación
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

def suma(numero1,numero2): #para crear una función es necesaria la palabra reservada "def" con el nombre de la función y variables
    resultado = numero1 + numero2 #creamos una variable que almacene el resultado de los numeros
    print("La suma de",numero1,"con",numero2,"es:",resultado) #imprimimos el valor de las sumas

suma(15,15) #llamamos a la función incluyendo sus variables para la suma, al igual que los otros dos casos

suma(25,25)

suma(50000,7000)

#Practica: 034_Funciones_Argumentos_arbitrarios
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

#¿Cuántos argumentos se utilizan en cada una de estas llamadas?  Hay 10 argumentos

#def colores(*args):
#	pass

#colores('rojo', 'azul', 'verde', 'amarillo')
#colores('lila', 'negro', 'rojo')
#colores('rosa')
#colores('marrón', 'naranja')

def colores(*args): #definimos la función colores con un numero arbitrario de elementos
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.') #imprimimos el valor de la posición 1 y 0

col_var = ["azul", "rojo"] #creamos una lista con dos atributos
colores(*col_var) #mandamos llamar la función con la lista como atributos

def suma(*args): #creamos la función suma con elementos arbitrarios
    resultado = 0 #creamos la variable resultado y la igualamos a 0
    for x in args: #creamos un bucle for que recorre los argumentos arbitrarios
        resultado += x #cada que recorre el bucle suma un nuevo elemento
    print("El resultado de la suma de los cinco numeros es:",resultado) #imprimimos el resultado de la suma

numeros = [10, 20, 30, 40 ,50] #creamos una lista con diferentes numeros

suma(*numeros) #llamamos a la función suma usando la lista numeros como elementos arbitrarios de la función

#Practica: 035_Funciones_Diccionarios_arbitrarios
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

def colores (**kwargs): #en esta función usamos un diccionario arbitrario con **kwargs
	print("Este es el color " + kwargs['color1'] + '.') #imprimimos el valor del color1

colores(color1='rojo', color2='azul') #creamos un diccionario con las variables de colores

def suma(x, y): #creamos una función con dos variables 
    return x + y #hacemos la sima de las variables y las regresamos al programa

total = suma(10,10) #recibimos en una varible el retorno de la función
print(total) #imprimimos el resultado de la operaciónS
