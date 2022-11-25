# -*- coding: utf-8 -*-

# Primero importar librerias
import os, sys

# Declarar variables

opcion = -1

# Declarar funciones/procedimientos/....

def consultarContacto(file, name):
    try:
        f = open(file,"r")
    except FileNotFoundError:
        return "Primero debes crear el archivo"
    else:
        directorio = f.readlines()
        f.close()
        directorio = dict([tuple(line.split(",")) for line in directorio])
        if name in directorio:
            return ("Nombre: "+ name +"  Teléfono: " + directorio.get(name))
        else:
            return ("El contacto " + name + " no está en la agenda")


def eliminarContacto(file, nombre):
    try:
        f = open(file,"r+")
    except FileNotFoundError:
        return "Primero debes crear el archivo"

def anadirContacto(file, name, phone):
    try:
        with open(file,"r+") as f:
            contenido = f.read()
            f.write(name+","+phone+"\n")
            print("Contacto añadido con éxito")
            f.close()
    except FileNotFoundError:
        return "Primero debes crear el archivo"

def crearVaciarFichero(file):
    if os.path.exists(file):
        print("El fichero ya existe")
        answer = input("El fichero " + file + " ya existe. ¿Desea vaciarlo [S/N]?\n")
        if answer.upper() == "N":
            return "No se ha vaciado el fichero\n"

    f = open(file, "w")
    f.close()
    print("Se ha creado el fichero para la agenda.\n")

def menu():
    print("Gestión de agenda telefónica")
    print("======================================")
    print("1. Consultar contacto")
    print("2. Añadir contacto")
    print("3. Eliminar contacto")
    print("4. Crear Agenda")
    print("5. Salir")
    opcn = int(input("Elige una opcion \n"))
    return opcn

def lanzarPrograma():

    """
    Función aue lanza las opciones del menú de la aplicación para la gestión de la agenda telefónica
    """
    fichero = "MiAgenda.txt"

    while True:
        opcion = menu()

        if opcion == 1:
            #1. Consultar contacto
            nombre = input("Introduce el nombre del contacto que quieres buscar\n")
            print(consultarContacto(fichero,nombre))

        elif opcion == 2:
            #2. Añadir contacto
            nombre = input("Introduce el nombre del contacto: \n")
            telefono = int(input("Introduce el número de teléfono del contacto: \n"))
            print(anadirContacto(fichero,nombre,str(telefono)))

        elif opcion == 3:
            #3. Eliminar contacto
            print("Eliminando contacto\n")

        elif opcion == 4:
            #4. Crear Agenda
            print(crearVaciarFichero(fichero))

        elif opcion == 5:
            #5. Salir
            print("Terminando programa\n")
            break
        else:
            print("Opción incorrecta. Por favor, inténtalo de nuevo\n")

        print("\n")


#---------------------- Programa principal ---------------------------

lanzarPrograma()