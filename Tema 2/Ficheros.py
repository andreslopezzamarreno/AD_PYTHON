
''''#!/usr/bin/env python
# -*- coding:utf-8 -*-
#forma clasica de crear un archivo:

#creamos el archivo
#f = open("archivotext.txt","w")

#otra forma de crear archivo
with open ("archivotext.txt","w") as f:

    #escribimos en el
    f.write("creando archivo de texto en python de forma clasica 2")

#cerramos el archivo
f.close()'''

"""
Escribe un programa en python que escirba de la forma clisica en un fichero llamado 'ficheroenpython.txt'
el siguiente mensaje:
este fichero es mi primer programa en fichero y lo he escrito en python usando la forma clasica , que es la siguiente
f = open()
f.write()
f.close()
"""

'''f = open("ficheroenpython.txt","w")
f.write("este fichero es mi primer programa en fichero y lo he escrito en python usando la forma clasica , que es la siguiente:"
        "\nf = open()"
        "\nf.write()"
        "\nf.close()")
f.close()'''

"""
ahora con 
with open()as f
f.write()
f.close()
"""

'''with open("ficheroenpython.txt","w") as f:

#escribimos en el
        f.write("este fichero es mi primer programa en fichero y lo he escrito en python usando la \nforma clasica , que es la siguiente:"
        "\nwhith open() as f"
        "\nf.write()"
        "\nf.close()")
#cerramos el archivo
f.close()'''

'''with open("ficheroenpython.txt","r") as f:
        texto = (linea for i, linea in enumerate(f) if i>= 0 and i<=3)
        for linea in texto:
                print(linea)'''

'''with open ("ficheroenpython.txt","r+") as f:
        #contenido = f.read() #con f.read antes escribimos al final, sin eso escribimos al principio
        f.write("escribiendo una linea al final\n")
f.close()'''

'''with open ("ficheroenpython.txt","a") as f:
        for a in range(8):
                f.write("\notra opcion")
f.close()'''

'''lista = ["\nEscribiendo\n", "listas \n", "en fichero"]
with open("ficheroenpython.txt","r+") as f :
        contenido = f.read()
        f.writelines(lista)
f.close()'''

#modifica lon de arriba para que haga lo mismo sin usar r+
'''lista = ["\nEscribiendo\n", "listas \n", "en fichero"]
with open("ficheroenpython.txt","a") as f:
        #contenido = f.read()
        f.writelines(lista)
f.close()'''


