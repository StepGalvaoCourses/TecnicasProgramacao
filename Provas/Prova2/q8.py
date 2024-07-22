tmp = 0
anterior = 0
proximo = 1
for n in range(5):
    tmp = proximo
    proximo = anterior + proximo
    anterior = tmp;
    print(proximo)