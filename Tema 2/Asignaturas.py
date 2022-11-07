
notas = []
asignaturas = ["a","b","c","d"]
media = 0

for iter in asignaturas:
    print("yo estudio "+ iter)

for cont in asignaturas:
    nota =input("Que notas tienes en " +cont)
    notas.append(nota)

for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " tienes un " + notas[i])

for i in notas:
   media += int(i)

print("La media es: " + str(media/len(notas)))
