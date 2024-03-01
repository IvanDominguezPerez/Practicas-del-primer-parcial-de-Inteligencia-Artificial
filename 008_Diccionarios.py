#008_Diccionarios

#Practica: 030_Diccionarios_Metodo_DICT
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

teclado2 = { #declaramos un diccionario llamado teclado2 en el que almacenamos tres características como se ven a continuación
    "Categoría": "Teclados",
    "Modelo": "Corsair K55 RGB",
    "Precio": "59,99"
    }

mostrar = teclado2["Modelo"]  #en la variable mostrar almacenamos el modelo y precio del teclado
mostrar2 = teclado2["Precio"]
print("El modelo de teclado es:",mostrar,"y tiene un precio de:",mostrar2) #imprimimos la variable para mostrar que fue lo que guardamos

#mostrar = dict(teclado2) //esta seria la forma de almacenar todo lo que hay en el diccionario

#Practica: 031_Diccionarios_Bucle_For
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

#para mostrar un diccionario entero basta con asignarlo todo a un print // print(teclado1)
#para hacer modificaciones en el diccionario // teclado1["Precio"] = 85

teclado1 = { #copiamos los diccionarios precargados
	'Categoría': 'Teclados.',
	'Modelo': 'HyperX Alloy FPS Pro.',
	'Precio': '89,99.'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

for x, y in teclado1.items(): #creamos un bucle for para mostrar los atributos del diccionario
	print(x,"=",y) #la variable x muestra característca y la y muestra el contenido
#con la función items nos permite tener tanto el atributo como su contenido

#Practica: 032_Diccionarios_Metodos
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

#para saber cuantos atributos hay en un diccionario // print(len(teclado1))

#para eliminar atributos // teclado1.pop("Categoría")

#para eliminar todo el diccionario // del teclado1

#para vaciar un diccionario // teclado1.clear()

#para añadir atributos // teclado1["Color"]="Negro"

#para copiar un diccionario // teclado_copia = teclado1.copy()

teclado1 = { #copiamos los diccionarios precargados
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1 #eliminamos por completo el diccionario teclado1
teclado2.pop("Categoría") #eliminamos el atributo de "Categoría" del diccionario teclado2
teclado2.pop("Precio") #eliminamos el atributo de "Precio" del diccionario teclado2
print(teclado2) #imprimimos el atributo restante del diccionario teclado2
