#007_Bucles

#Practica: 026_Bucles_While
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

x = 0 #declaramos la variable x y le asignamos el valor de 0
while x < 15: #creamos un bucle while que se repetira mienatras x sea menor a 15
    x += 5 #sumamos 5 al valor de x
    print("x ha incrementado en 5\n") #imprimimos que x a aumentado su valor en 5

print("x ha llegado a 15\n") #imprimimos que se ha terminado el bucle

x = 0 #asignamos 0 a x de nuevo
while x > -100: #creamos un bucle que seguira hasta que x sea -100
    x += -20 #decrementamos x en 20 unidades
    print("Se le han restado 20 a x\n") #imprimimos cada que x tenga una reducción

print("x ha llegado a -100\n") #notificamos que salimos del bucle

x = 10 #asignamos en valor 10 a x
while x >= 0: #creaos un bucle que se repetira mientras x valga mas o igual a 0
    print("El valor de x es",x,"\n") #imprimimos los valores actuales de x 
    x += -1 #decrementamos el valor de x

print("El programa ha finalizado")#imprimimos el final de el programa

#Practica: 027_Bucles_While_IF
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

x = 0 #declaramos una variable x y le asignamos el valor de 0
while x <= 30: #creamos un bucle while con condicion de x ser menor o igual a 30
    x += 1 #sumamos 1 al valor de x
    if x == 15: #creamos un if en el que si el valor de x es 15 acabe con el bucle
        print("Se rompio la ejecución del bucle cuando x valia",x) #imprimimos que acabamos el bucle
        break #acabamos el bucle
    if x == 4 or x == 6 or x == 10: #creamos un condicional en caso de que x sea 4, 6 o 10 en el que nos saltamos lo que queda del bucle
        print("Se ha saltado el valor de",x,"\n") #imprimimos que nos saltamos el bucle
        continue #continuamos con el bucle sin seguir
    print("El valor del bucle es:",x,"\n")#imprimimo el valor de x en el bucle

#Practica: 028_Bucles_For
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

colores = ('rojo','azul','verde','amarillo')
for x in colores:
    print("El color es:",x,)

#Practica: 029_Bucles_For_Range
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

for x in range(7,700,100): #creamos un bucle for parax que con la función range empieza en 7, llegara hasta el 700 en incrementos de 100
    print("El valor de x es:",x) #imprimimos el valor de x cada que se repita el bucle
