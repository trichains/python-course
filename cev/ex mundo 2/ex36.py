valor_casa_entrada=float(input('Qual o valor da casa que você deseja comprar? R$'))
salario_entrada=float(input('Qual o seu salário? R$'))
valor_parcela_entrada=int(input('Em quantos anos você quer pagar a casa? R$'))*12

prestacao_mensal = valor_casa_entrada / valor_parcela_entrada
limite = (salario_entrada * 0.3)

if prestacao_mensal > limite:
    print('Desculpe, o empréstimo para a compra desta casa foi negado...')
else:
    print('Parabéns, o empréstimo para a compra desta casa foi aprovado!')
    print(f"O valor da prestação mensal será de R${prestacao_mensal:.2f}.")