#015_Excepciones

#Practica: 050_Excepciones
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

variable = "Correcto." #declaramos una variable y le asignamos un string

try: #probamos imprimir la variable
    print(variable)
except: #si la variable no esta declarada mostrara la siguiente secuencia
    print("La variable no está declarada.")

try: #probamos otra vez pero con una variable inexistente y podremos ver que ahora isa el except
    print(varia)
except:
    print("La variable no está declarada.")
