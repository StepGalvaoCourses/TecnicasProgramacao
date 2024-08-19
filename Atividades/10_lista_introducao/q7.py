notas = []

for i in range(5):
    nota = float(input("Digite a nota:"))
    notas.append(nota)

media = (notas[0] + notas[1] + notas[2] + notas[3] + notas[4])/5
print(media)