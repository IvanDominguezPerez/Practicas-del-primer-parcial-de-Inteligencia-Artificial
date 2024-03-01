#002_Strings

#Practica: 002_Strings
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

Ivar1 = "String con comillas dobles" #Creamos una variable y almacenamos un string con comillas dobles
Ivar2 = 'String con comillas simples' #Creamos una variable y almacenamos un string con comillas simples
Ivar3 = '"print()" se utiliza para imprimir valores en la consola' #Creamos una variable y almacenamos la frase con comillas simples
#para evitar el problema de tener dentro del string comillas dobles
print(Ivar3) #Imprimimos el valor de la variable 3 en la consola

#Practica: 003_Strings_Concatenar
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

Ivar1 = "Hola, ¿cómo " + "estas?" #Creamos una variable y concatenamos dos strings en ella
print(Ivar1) #Imprimimos el valor de la variable Ivar1
Ivar2 = "Los Strings" #Creamos una variable y almacenamos un string
Ivar3 = "son geniales" #Creamos una variable y almacenamos un string
Ivar4 = Ivar2 + Ivar3 #Creamos una variable y concatenamos el contenido de las ultimas dos variables creadas
print(Ivar2 + " " + "son geniales") #Imprimimos el valor de una variable con un string
nombre1 = "Iván" #creamos una variable y almacenamos el nombre
nombre2 = "Alejandro" #creamos una variable y almacenamos el segundo nombre
apellido1 = "Domínguez" #creamos una variable y almacenamos el apellido
apellido2 = "Pérez" #creamos una variable y almacenamos el segundo apellido
nombre_completo = nombre1 + " " + nombre2 + " " + apellido1 + " " + apellido2 + "." #En una tercera variable concatenamos el nombre completo con espacios
print(nombre_completo) #imprimimos la variable nombre_completo
numero = '2131' + '0234' #Concatenamos dos numeros (no sumarlos)
print(numero) #imprimimos la variable numero

#Practica: 004_Strings_metodos_upper_lower_title
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

Ivar1 = "iván alejandro domínguez pérez" #Creamos una variable y almacenamos un nombre todo en minúsculas
Ivar1 = Ivar1.title() #Le aplicamos el metodo title() que sirve para que la primera letra de cada palabra cambia a mayúscula
print(Ivar1) #Imprimimos la variable Ivar1
Ivar2 = "Esta Es Una Frase Para Ser Formateada" #Creamos una variabe y almacenamos la respectiva frase
Ivar2 = Ivar2.lower() #Le aplicamos el metodo lower() que sive para dejar todas las letras del string en minúsculas
print(Ivar2) #Imprimimos la variable Ivar2
Ivar3 = "Esta Es Una Frase Para Ser Formateada" #Creamos una variabe y almacenamos la respectiva frase
Ivar3 = Ivar3.upper() #Le aplicamos el metodo upper() que sive para dejar todas las letras del string en mayúsculas
print(Ivar3) #Imprimimos la variable Ivar3
#Los métodos se pueden aplicar dentro de los print para agilizar el código y tener menos líneas

#Practica: 005_Strings_Saltos_de_linea_y_tabulaciones
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

print("-Python.\n-JavaScript.\n-Java.\n-PHP.\n-TypeScript.\n-SQL.\n-COBOL.\n-C.\n-C++.\n")
#Vamos a imprimir una lista de lenguajes de programación, solo que haciendolo en la misma línea, por lo que usaremos \n lo cual nos permite
#cambiar de renglon pero escribiendo en la misma linea del print().
#También tenemos \t la cual nos permite hacer una tabulación cuando los pongamos.
