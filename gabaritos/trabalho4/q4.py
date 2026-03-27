# Questão 4: Imposto sobre Salário
salario = float(input("Digite o salário: "))

if salario > 1250:
    imposto = salario * 0.15
else:
    imposto = salario * 0.10

print(f"Imposto = R$ {imposto}")