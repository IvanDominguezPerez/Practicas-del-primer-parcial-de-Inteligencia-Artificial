#006_Condicionales

#Practica: 020_Condicionales_If
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

#Tenemos 3 ejercicios copiados del ejemplo para hacer las respectivas modificaciones
#en el primer ejercicio tenemos que cambiar el operador el if para que la condición se cumpla "True"
num1 = 15 #asignamos un numero a cada variable
num2 = 20

if num1 != num2: #en este condicional decimos que si el valor de las variables es diferente se cumple la condición 
	print('Se ejecuta el if.')

#en el segundo ejercicio tenemos que cambiar el operador el if para que la condición se cumpla "True"
num1 = 1450 #asignamos un numero a cada variable
num2 = 60

if num1 > num2: #en este condicional decimos que si el valor de num1 es mayor que el de num2 se cumple la condición
	print('Se ejecuta el if.')

#en el tercer ejercicio tenemos que hacer que la condición no se cumpla "False" sin cambiar el operador
num1 = 60 #asignamos un numero a cada variable
num2 = 60

if num1 != num2: #en este condicional decimos que si el valor de las variables es diferente se cumple la condición 
	print('Se ejecuta el if.')

#si las condiciones se cumplen se ejectutan las instrucciones que estan abajo de manera tabulada

#Practica: 020_Condicionales_If
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

#Tenemos 3 ejercicios copiados del ejemplo para hacer las respectivas modificaciones
#en el primer ejercicio tenemos que cambiar el operador el if para que la condición se cumpla "True"
num1 = 15 #asignamos un numero a cada variable
num2 = 20

if num1 != num2: #en este condicional decimos que si el valor de las variables es diferente se cumple la condición 
	print('Se ejecuta el if.')

#en el segundo ejercicio tenemos que cambiar el operador el if para que la condición se cumpla "True"
num1 = 1450 #asignamos un numero a cada variable
num2 = 60

if num1 > num2: #en este condicional decimos que si el valor de num1 es mayor que el de num2 se cumple la condición
	print('Se ejecuta el if.')

#en el tercer ejercicio tenemos que hacer que la condición no se cumpla "False" sin cambiar el operador
num1 = 60 #asignamos un numero a cada variable
num2 = 60

if num1 != num2: #en este condicional decimos que si el valor de las variables es diferente se cumple la condición 
	print('Se ejecuta el if.')

#si las condiciones se cumplen se ejectutan las instrucciones que estan abajo de manera tabulada

#Practica: 022_Condicionales_If_Elif_Else_Entradas_datos
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

edad = int(input('¿Cuál es tu edad?\n')) #empezamos solicitando la edad del usuario con la función input y guardando el  valor en una variable entera.
if edad <= 0: #empezamos los condicionales con un if en el que si la edad es 0 o menor arroja el mensaje siguiente
    print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 17: #en este condicional modificamos el rango de edad de 1 a 17 usando un elif el cual nos permite seguir con las condiciones
    print('Eres menor de edad.') 
elif edad >= 18 and edad <= 45:
    print('Todavía eres joven.')
elif edad >= 46 and edad <= 100:
    print('Ya estas grande.')
elif edad > 100 and edad <= 120:
    print('Eres una reliquia andante')
else:
    print('Edad no válida.')
#Al final colocamos varias condicionales con varios mensaje que nos diran distintos mensajes dependiendo la edad que ingrese el usuario

#Practica: 023_Condicionales_Buscar_datos_en_listas_y_tuplas
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

colores = ('rojo', 'amarillo', 'azul', 'verde') #empezamos el programa creando una tupla con cuatro colores
entrada = input("¿Cuál es tu color favorito?:\n") #ingresamos un dato preguntandole al usuario su colo favorito
if entrada in colores: #creamos un condicional if en el que preguntamos si el color que eligio el usuario se encuentra en la tupla 
    print("El color ",entrada," esta en la lista de buenos colores") #en caso de estar imprime el siguiente mensaje
else: #en caso de no estar imprime el siguiente mensaje
    print("Vaya color mas feo que elegiste")

#Practica: 024_Condicionales_Multiples_condicionales_IF
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

entrada = int(input('Introduce un número del 1 al 4:\n')) #primeramente preguntamos al usuario por un numero y lo guardamos en la variable
#entera entrada

if entrada == 1: #creamos cuatro condicionales con su respectivo print que nos indica que numero se ha seleccionado
    print('Has seleccionado la opción número 1.')
if entrada == 2:
    print('Has seleccionado la opción número 2.')
if entrada == 3:
    print('Has seleccionado la opción número 3.')
if entrada == 4:
    print('Has seleccionado la opción número 4.')

#Practica: 025_Condicionales_Sintaxis_reducida
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

x = 10000 #declaramos dos variables y les asignamos valores
y = 200

print('x es menor que y.') if x < y else print('x no es menor que y') #esta es la forma en la que se colocan un if y else en la misma linea

#podemos usar and y or en los condicionales cuando los necesitemos y evaluar mas condcines en el mimso if
