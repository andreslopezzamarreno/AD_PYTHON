def segundo_numero(numero):
    if numero == 1:
        leido = 'un'
    elif numero == 2:
        leido = 'dos'
    elif numero == 3:
        leido = 'tres'
    elif numero == 4:
        leido = 'cuatro'
    elif numero == 5:
        leido = 'cinco'
    elif numero == 6:
        leido = 'seis'
    elif numero == 7:
        leido = 'siete'
    elif numero == 8:
        leido = 'ocho'
    elif numero == 9:
        leido = 'nueve'
    return leido

def escribir_numero(numero):
    #De la forma de arriba tengo en la posicion 0 las decenas y en la posicion 1 las unidades
    digitos = [int(a) for a in str(numero)]

    if len(digitos) == 1:
        leido = segundo_numero(numero)
    elif len(digitos) == 2:

        #otra forma
        unidades = numero %10
        decenas = (numero%100-numero%10)//10

        if digitos[0] == 1:
            if digitos[1] > 5:
                leido = 'dieci' + segundo_numero(digitos[1])
            elif digitos[1] == 4:
                leido = "catorce"
            elif digitos[1] == 3:
                leido = "trece"
            elif digitos[1] == 2:
                leido = "doce"
            elif digitos[1] == 1:
                leido = "once"
            elif digitos[1] == 0:
                leido = "diez"
        if digitos[0] == 2:
            if digitos[1] == 0:
                leido = "veinte"
            else:
                leido = 'veinti'+ segundo_numero(digitos[1])
        if digitos[0] == 3:
            if digitos[1] == 0:
                leido = "treinta"
            else:
                leido = 'treinta y '+ segundo_numero(digitos[1])
        if digitos[0] == 4:
            if digitos[1] == 0:
                leido = "cuarenta"
            else:
                leido = 'cuarenta y '+ segundo_numero(digitos[1])
        if digitos[0] == 5:
            if digitos[1] == 0:
                leido = "cincuenta"
            else:
                leido = 'cincuenta y '+ segundo_numero(digitos[1])
        if digitos[0] == 6:
            if digitos[1] == 0:
                leido = "sesenta"
            else:
                leido = 'sesenta y '+ segundo_numero(digitos[1])
        if digitos[0] == 7:
            if digitos[1] == 0:
                leido = "setenta"
            else:
                leido = 'setenta y '+ segundo_numero(digitos[1])
        if digitos[0] == 8:
            if digitos[1] == 0:
                leido = "ochenta"
            else:
                leido = 'ochenta y '+ segundo_numero(digitos[1])
        if digitos[0] == 9:
            if digitos[1] == 0:
                leido = "ochenta"
            else:
                leido = 'noventa y '+ segundo_numero(digitos[1])
    else:
        print('numero demasiado largo(mas de 2 digitos)')

    return leido

diccionario = {
    'nombre': input("¿nombre?"),
    'apellido': input("¿Primer apellido?"),
    'edad': int(input("¿edad?")),
    'telefono': int(input("¿Telefono?"))
}

print(f"{diccionario['nombre']} {diccionario['apellido']} tiene {escribir_numero(diccionario['edad'])} años y su telefono es {diccionario['telefono']}")