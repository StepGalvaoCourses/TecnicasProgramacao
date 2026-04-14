nota = float(input("Digite a nota (0-10): "))

if nota >= 9 and nota <= 10:
    print("A")
if nota >= 7 and nota < 9:
    print("B")
if nota >= 5 and nota < 7:
    print("C")
if nota >= 3 and nota < 5:
    print("D")
if nota < 3:
    print("E")