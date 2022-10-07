# pregunta la edad y el precio de la entrada depende de ella

edad = int(input("Que edad tienes"))

if edad <= 4:
    precio = 0
elif edad <= 18:
    precio = 5
else:
    precio = 10

print("El precio de la entrada es:", precio)
