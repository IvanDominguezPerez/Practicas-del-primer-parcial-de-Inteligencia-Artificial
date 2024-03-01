#004_Listas

#Practica: 009_Listas_Creacion_Utilizacion
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"] #Este es el ejemplo de creación de una lista
print("De la siguiente lista, ¿Qué color esta en la posición 3?") #imprimimos la pregunta sobre las listas
print(colores) #imprimimos la lista
print("El color en la posición 3 es el: AMARILLO") #respondemos la pregunta
print("¿En qué posición se encuentra el color 'rojo'? ¿y el 'rosa'?\nEl color 'rojo esta en la posición 0 y el rosa en la 7") #hacemos otra pregunta
#y la resolvemos
lista = ["tres", "dos", "cinco", "cuatro", "uno"] #creamos una lista basada en saber ordenar segun las listas
print(lista) #imprimimos la lista creada segun las instrucciones
print(lista[2]) #esta es la forma de imprimir un segmento de la lista deseada

#NOTA: En las listas empezamos a contar desde el "0"

#Practica: 010_Listas_Posiciones_negativas
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #aqui tenemos la lista de colores precargada
print(colores[-1],"\n",colores[-7],"\n",colores[-5],"\n",colores[-2],"\n",colores[-10]) #accedemos e imprimimos los colores solicitados usando las
#posiciones negativas como se muestra, (la ultima variables es -1)

#Practica: 011_Listas_Eliminar_elementos
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #cargamos la lista previamente hecha
del colores[1]  #en esta y las tres lineas siguientes eliminamos un atributo de la lista segun su posición ya sea positiva o negativa
del colores[-6]
del colores[-4]
del colores[-3]
print(colores)  #imprimimos la lista actualizada sin los colores que eliminamos

#Practica: 012_Listas_Eliminar_elementos_remove
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #copiamos la lista precargada
colores.remove('amarillo') #en esta y la siguiente linea borramos un atributo de la lista con la función remove, con la cual podemos poner el nombre
colores.remove('rojo')
print(colores) #imprimimos la lista actualizada sin los atributos que fueron eliminados

#Practica: 013_Listas_Eliminar_elementos_pop
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #copiamos la lista precargada
eliminado1 = colores.pop(1) #en esta y la siguiente linea eliminamos un elemento de la lista colores, pero guardamos cada elemento en una variable
eliminado2 = colores.pop(-2)
print("La lista colores actualizada es: ",colores) #imprimimos la lista colores actualizada sin los elementos borrados
nueva_lista = [eliminado1, eliminado2] #creamos una lista con los elementos eliminados que estan en variables
print("La lista de colores eliminados es: ",nueva_lista) #imprimimos la lista con los elementos eliminados

#Practica: 014_Listas_Insertar_elementos_append
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #copiamos la lista precargada
colores.append("fuxia") #en esta y la siguiente linea insertamos un atributo a la lista colores con la función append()
colores.append("celeste") #NOTA: append() solo agrega atributos al final de la lista
print("La lista con colores agregados es: ",colores) #imprimimos la lista actualizada con los colores agregados

#Practica: 015_Listas_Insertar_elementos_insert
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #copiamos la lista precargada
colores.insert(-4,"magenta") #en esta y la siguiente linea insertaremos un atributo a la lista usando solo posiciones negativas
colores.insert(-1,"turquesa") #la característica de insert() es que podemos elegir donde colocar el nuevo atributo
print(colores) #imprimimos la lista actualizada con los nuevos colores agregados donde deseamos

#Practica: 016_Listas_Ordenar_elementos_sort
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #copiamos la lista precargada
colores.sort(reverse=True) 
print(colores) #imprimimos la lista actualizada de manera alfabetica inversa (de z a la a)
#el metodo sort() sirve para organizar una lista de forma alfabetica
#la forma en que se coloco se usa para cuando deseamos que se ordene al inverso del alfabeto
#en cambio cuanso usamos sorted(lista) que podemos usar simplemente en un print() este cambio durara solo ese momento
#sort es permanente

#Practica: 017_Listas_Contar_elementos
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #copiamos la lista precargada
cuantos_colores = len(colores) #asiganamos a una variable el numero de colores
print("El numero de colores en la lista colores es de: ",cuantos_colores) #imprimimos el numero de colores que hay en la lista
