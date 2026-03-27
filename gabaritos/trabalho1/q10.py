# Questão 10: Salário do Fulano (INSS 15% e IR 10%)
salario_bruto = 5000.00
inss = salario_bruto * 0.15
irpf = salario_bruto * 0.10
salario_liquido = salario_bruto - inss - irpf

print("Salário Bruto:", salario_bruto)
print("Desconto INSS:", inss)
print("Desconto IR:", irpf)
print("Salário Líquido:", salario_liquido)