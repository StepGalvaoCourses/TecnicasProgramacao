# Questão 6: Quota de Internet (OBI 2021)
cota = int(input("Quota mensal (X): "))
meses = int(input("Quantidade de meses: "))
total_usado = int(input("Total usado nos N meses: "))


# A quota disponível para o próximo mês é a soma de todas as quotas 
# mensais (incluindo o próximo mês) menos o que já foi usado.
excesso = (cota * meses) - total_usado
proximo_mes =  cota + excesso
print(f"Você pode usar {proximo_mes} no próximo mês.")