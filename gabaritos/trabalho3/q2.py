# Questão 2: Contracheque IFPI Softwares
matricula = input("Matrícula: ")
salario_base = float(input("Salário Base: "))
irpf = salario_base * 0.075
inss = salario_base * 0.14
salario_liquido = salario_base - irpf - inss
print("------------------------------------------------------------")
print("CONTRACHEQUE - IFPI SOFTWARES")
print("------------------------------------------------------------")
print(f"Funcionário (Matrícula): {matricula}")
print(f"Salário Base: R$ {salario_base}")
print("------------------------------------------------------------")
print(f"(-) IRPF (7.5%): R$ {irpf}")
print(f"(-) INSS (14%): R$ {inss}")
print("------------------------------------------------------------")
print(f"SALÁRIO LÍQUIDO: R$ {salario_liquido}")
print("------------------------------------------------------------")