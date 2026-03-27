# Questão 5: Raízes de Equação do Segundo Grau (Delta)

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

delta = (b ** 2) - (4 * a * c)

if delta > 0:
    print("2 raízes")
if delta == 0:
    print("1 raiz")
if delta < 0:
    print("0 raízes")