#010_POO

#Practica: 036_POO_Clases_Objetos
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

class Usuario: #creamos la clase usuario
	nombre = '' #creamos atributos de la clase
	apellidos = ''

	def imprime_datos(self): #creamos la función de la clase imprime_datos
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos) #imprimimos los datos del usuario

usuario001 = Usuario() #creamos un objeto de la clase usuario

usuario001.nombre = 'Enrique' #ingresamos el nombre del usuario
usuario001.apellidos = 'Barros Fernández' #ingresamos el apellido del usuario

usuario001.imprime_datos() #llamamos a la función imprime_datos del objeto creado de la clase Usuario

#Practica: 037_POO_Metodo_init
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

class Usuario: #creamos la clase Usuario
    def __init__(self, nombre, apellidos): #con el metodo init solicita la información al crear el objeto
        self.nombre = nombre #asignamos el nombre de los usuarios
        self.apellidos = apellidos

    def imprime_datos(self): #creamos una función para imprimir el nombre
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario('Enrique', 'Barros Fernández') #esta es la forma de crear objetos usando el init

usuario002 = Usuario('Javier', 'Gomila Reyes')

#Practica: 038_POO_Self
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

class Usuario: #creamos la clase Usuario
    def __init__(self, nombre, apellidos): #definimos el método  que incluye el nombre y apellido
        self.nombre = nombre #asignamos el nombre
        self.apellidos = apellidos #asignamo el apellifo

    def imprime_datos(self): #creamos un metodo para imprimir los datos
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos) #imprimimos los datos del usuario

usuario001 = Usuario('Enrique', 'Barros Fernández') #ingresamos los datos del usuario creando un objeto

usuario002 = Usuario('Javier', 'Gomila Reyes') #Creamos otro usuario e introducimos sus datos

usuario002.nombre = 'Jacinto' #cambiamos el nombre del usuario 

usuario002.imprime_datos() #mostramos los cambios hechos en el usuario

#Practica: 039_POO_Eliminar_objetos
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

class NombreClase: #usando el pass podemos crear una clase vacía
	pass

#del nombre_objeto.atributo //esta es la forma de eliminar atributos de un objeto

#del nombre_objeto //esta es la forma de eliminar objetos

#Practica: 040_POO_Herencias
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

# Esta es la superclase
class Usuarios: #creamos la clase principal
    def __init__(self, nombre, apellidos): #usamos la base de las clases anteriores
        self.nombre = nombre
        self.apellidos = apellidos

    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

# Esta es la subclase
class UsuariosPremium(Usuarios): #esta clase contiene todo lo de la clase principal pero le
	pass #podemos agregar incluso mas cosas

#Practica: 041_POO_Heredar_propiedades
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Las cuantro lineas de arriba tienen la función de poder colocar acentos

# Esta es la superclase
class Usuarios: #copiamos la superclase ya definida
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

# Esta es la subclase
class UsuariosPremium(Usuarios): 
    def __init__(self, nombre, apellidos, instagram): #aqui es como heredamos las propiedades que
        Usuarios.__init__(self, nombre, edad) #queremos de la superclase sin necesidad de repetirlas
        self.instagram = instagram
