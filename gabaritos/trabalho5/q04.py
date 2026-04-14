categoria = input("Digite a categoria (E-Estudante, A-Aposentado, P-Professor ou R-Regular): ")

if (categoria == "E" or categoria == "A"):
    print("Meia-entrada: R$ 10,00")
else:
    print("Entrada normal: R$ 20,00")