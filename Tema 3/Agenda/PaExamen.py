MiDiccionario = {
    'Nombre' : "Harry",
    'Apellido': "Potter",
    'Edad' : 18,
    'Genero' : 'Masculino',
    'Padres' : ['James','Lili']}


'''Si lo que queremos es acceder a un clave concreta dentro de un campo
compuesto:'''
#devuelve James y Lili (índice desde 0 hasta 2)
print(MiDiccionario["Padres"][0:2])
#devuelve James
print(MiDiccionario["Padres"][0:1])
#devuelve Lili
print(MiDiccionario["Padres"][1:2])
