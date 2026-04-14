valor_compra = float(input("Valor da compra: "))
idade = int(input("Idade do cliente: "))

if (valor_compra > 100 and idade > 60):
    print("Você tem direito ao desconto de veterano")
else:
    print("Pagamento pelo valor normal")