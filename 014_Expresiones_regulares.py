#014_Expresiones_regulares

#Practica: 046_Expresiones_regulares_SEARCH
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

import re #importamos el modulo de expresiones regulares

texto = "Bienvenidos a Programación fácil" #creamos una variable con un texto
busqueda = re.search("i", texto) #en una variable buscamos una letra que este
print(busqueda) #imprimimos la busqueda para ver el mach

texto = "Bienvenidos a Programación fácil" #basicamente hacemos lo mismo con letras, palabras pero tiene que ser exacto
busqueda = re.search("I", texto)
print(busqueda)

texto = "Bienvenidos a Programación fácil"
busqueda = re.search("Bienvenidos", texto)
print(busqueda)

#Practica: 047_Expresiones_regulares_FINDALL
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

import re #importamos el modulo de expresiones

texto = "tres tristes tigres comen trigo en un trigal" #creamos una variable con un texto
busqueda = re.findall("e", texto) #con findall buscamos todas las palabras qye contengan una e
print(busqueda)

import re

texto = "tres tristes tigres comen trigo en un trigal" #creamos una variable con un texto
busqueda = re.findall("es", texto) #con findall buscamos todas las palabras qye contengan una es
print(busqueda)

#Practica: 048_Expresiones_regulares_SPLIT_SUB
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

import re #importamos el modulo de expresiones

texto = "tres tristes tigres comen trigo en un trigal" #asignamos un string a una variable
busqueda = re.split(" ", texto, 4) #asignamos a una variable el metodo split que en cuatro espacios de la variable detectara lo que tengan
print(busqueda) #las comillas // imprimimos la variable

texto = "tres tristes tigres comen trigo en un trigal" #asignamos un string a una variable
busqueda = re.sub(" ",  "-",  texto, 4) #asignamos a una variable el metodo sub que agregara lo que tengamos en el segundo encomillado
print(busqueda) # de la variable seleccionada y las veces que necesitemos
