print(f"Valor do imposto a pagar: {imposto}")

# Questão 12: Média e Frequência Calculadas
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
carga_horaria = float(input("Carga horária total da disciplina: "))
horas_faltas = float(input("Quantidade de horas de falta: "))

media = (n1 + n2 + n3) / 3
# Frequência = (Horas Presente / Carga Horária) * 100
frequencia = ((carga_horaria - horas_faltas) / carga_horaria) * 100

if media > 7 and frequencia > 75:
    print(f"Média: {media}, Frequência: {frequencia}% - Aprovado")
else:
    print(f"Média: {media}, Frequência: {frequencia}% - Reprovado")