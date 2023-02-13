# Recebendo o valor da casa desejada
valor_casa_entrada = float(input('Valor da casa (em R$): '))

# Recebendo o salário do usuário
salario_entrada = float(input('Salário do comprador (em R$): '))

# Recebendo o tempo desejado para pagamento da casa, em anos
valor_parcela_entrada = int(input('Quantos anos de financiamento? '))

# Calculando o número de parcelas (convertendo anos em meses)
parcelas = valor_parcela_entrada * 12

# Calculando a prestação mensal
prestacao_mensal = valor_casa_entrada / parcelas

# Definindo o limite de prestação mensal com base no salário do usuário
# (30% do salário)
limite = salario_entrada * 0.3

# Verificando se a prestação mensal é maior que o limite de pagamento
if prestacao_mensal > limite:
    # Se a prestação mensal for maior que o limite, exibe a mensagem de negação
    print(f"Para pagar uma casa de R${valor_casa_entrada:.2f} em {valor_parcela_entrada} anos\n"
          f"a prestação será de R${prestacao_mensal:.2f}.\n"
          f"Com o salário de R${salario_entrada:.2f},\n"
          f"o limite de prestação mensal é de R${limite:.2f}.\n"
          "Portanto, o empréstimo para a compra desta casa foi NEGADO!")
else:
    # Se a prestação mensal não for maior que o limite, exibe a mensagem de aprovação
    print(f"Para pagar uma casa de R${valor_casa_entrada:.2f} em {valor_parcela_entrada} anos\n"
          f"a prestação será de R${prestacao_mensal:.2f}.\n"
          f"Com o salário de R${salario_entrada:.2f},\n"
          f"o limite de prestação mensal é de R${limite:.2f}.\n"
          "Portanto, o empréstimo para a compra desta casa foi APROVADO!")
    