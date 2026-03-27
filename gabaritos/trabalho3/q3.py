
# Questão 3: Sistema de Folha - Vendas IFPI
matricula = input("Matrícula: ")
salario_base = float(input("Salário Base: "))
total_vendas = float(input("Total de Vendas: "))

comissao = total_vendas * 0.10
subtotal_bruto = salario_base + comissao
inss = salario_base * 0.14
irpf = subtotal_bruto * 0.075
total_descontos = inss + irpf
salario_liquido = subtotal_bruto - total_descontos

print("================================================================")
print("SISTEMA DE FOLHA - VENDAS IFPI")
print("================================================================")
print(f"Vendedor (Matrícula): {matricula}")
print("----------------------------------------------------------------")
print("PROVENTOS:")
print(f"(+) Salário Base: R$ {salario_base}")
print(f"(+) Comissão (10%): R$ {comissao}")
print("----------------------------------------------------------------")
print(f"SUBTOTAL BRUTO: R$ {subtotal_bruto}")
print("----------------------------------------------------------------")
print("DESCONTOS:")
print(f"(-) INSS (14% s/ base): R$ {inss}")
print(f"(-) IRPF (7.5% s/ tot): R$ {irpf}")
print("----------------------------------------------------------------")
print(f"TOTAL DE DESCONTOS: {total_descontos}")
print("----------------------------------------------------------------")
print(f"SALÁRIO LÍQUIDO: R$ {salario_liquido}")
print("================================================================")