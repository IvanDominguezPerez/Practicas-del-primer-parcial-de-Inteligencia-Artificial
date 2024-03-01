#005_Tuplas

#Practica: 018_Tuplas_creacion_funcionamiento
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja') #esta no es una lista, es una tupla
#podemos identificarla por los parentesis, ademas la característica mas importantes es que las tuplas no se pueden modificar de ninguna forma
print("La segunda posición de esta tupla es el color: ",colores[1])
numeros = (10, 1, 5, 11) #tupla copiada para ejercicio
operacion = numeros[0] + numeros[3] + numeros[2] - numeros[1]
print("El resultado de la operación con los numeros de la tupla es de: ",operacion)

#Practica: 019_Tuplas_tuplas_a_listas
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #copiamos la lista precargada
Itupla = tuple(colores) #creamos una variable y convertimos la lista en una tupla
print(Itupla) #imprimimos la tupla para comprobar que el proceso funcine
#si queremos convertir una tupla en una lista hacemos lo mismo pero cambiampos de "tuple" a "list"  
