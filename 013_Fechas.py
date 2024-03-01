#013_Fechas

#Practica: 044_Fechas_Modulo_datetime
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

import datetime #importamos el modulo de fechas

fecha = datetime.datetime.now() #asignamos a una variable la fecha exacta

print(fecha) #imprimimos la fecha

fecha = datetime.datetime(2020, 9, 29, 19, 45) #asignamos a la variable la fecha que deseamos

print(fecha) #imprimimos la fecha

#Practica: 045_Fechas_Modulo_strftime
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

import datetime, locale #importamos modulos de tiempo y locación

locale.setlocale(locale.LC_ALL, "es-ES") #linea que cambia el idioma a español

ahora = datetime.datetime.now() #guardamos la fecha en la variable ahora

print(ahora.strftime("Día de la semana abreviado: %a ")) #en cada linea se especifica como mostrar una parte
print(ahora.strftime("Día de la semana completo: %A ")) #de le fecha usando
print(ahora.strftime("Mes abreviado: %b "))
print(ahora.strftime("Mes abreviado: %B "))
print(ahora.strftime("Fecha completa: %c "))
print(ahora.strftime("Siglo (empieza a contar desde cero): %C "))
print(ahora.strftime("Día del mes (01 - 31): %d "))
print(ahora.strftime("Día/hora/año: %D "))
print(ahora.strftime("Día del mes (1 - 31): %e "))
print(ahora.strftime("Año en dos dígitos: %g "))
print(ahora.strftime("Año en cuatro dígitos: %G "))
print(ahora.strftime("Mes abreviado: %h "))
print(ahora.strftime("Hora (00 - 23): %H "))
print(ahora.strftime("Hora (01 - 12): %I "))
print(ahora.strftime("Día del año: %j "))
print(ahora.strftime("Mes del 01 al 12: %m "))
print(ahora.strftime("Minuto: %M "))
print(ahora.strftime("Salto de línea: %n"))
print(ahora.strftime("AM o PM: %p "))
print(ahora.strftime("Hora + AM o PM: %r"))
print(ahora.strftime("Hora y minutos: %R"))
print(ahora.strftime("Segundos: %S"))
print(ahora.strftime("Tabulación: %t"))
print(ahora.strftime("Hora, minutos y segundos: %T"))
print(ahora.strftime("Día de la semana (número): %u"))
print(ahora.strftime("Semana del año (empieza en domingo): %U"))
print(ahora.strftime("Semana del año(Condiciones especiales): %V"))
print(ahora.strftime("Semana del año (empieza en lunes): %W"))
print(ahora.strftime("Día de la semana (empieza en domingo): %w"))
print(ahora.strftime("Día/mes/año de dos dígitos: %x"))
print(ahora.strftime("Hora/minutos/segundos: %X"))
print(ahora.strftime("Año corto: %y"))
print(ahora.strftime("Año largo: %Y"))
