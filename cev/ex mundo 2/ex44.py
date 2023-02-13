# Primeiro, solicitamos ao usuário que informe o preço normal do produto
preco_normal = float(input("Informe o preço normal do produto: "))

# Em seguida, apresentamos as opções de pagamento ao usuário
print(f'''
| {'FORMAS DE PAGAMENTO':^26} |
| [1] À vista dinheiro/cheque|
| [2] À vista no cartão      |
| [3] Em até 2x no cartão    |
| [4] 3x ou mais no cartão   |
''')

# Depois, solicitamos ao usuário a escolha da condição de pagamento
condicao = int(input("Digite a condição do valor: "))

# Verificamos a condição escolhida e calculamos o preço a ser pago
if condicao == 1: # Será acrescentado 10% de desconto
    preco = preco_normal - (preco_normal * 0.1)
elif condicao == 2: # Será acrescentado 5% de desconto
    preco = preco_normal - (preco_normal * 0.05)
elif condicao == 3: # Sem desconto ou juros
    preco = preco_normal
    parcela = preco / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} sem juros.')
# Verifica se a condição escolhida é 4
elif condicao == 4:
    parcelas = int(input('Quantas parcelas?: ')) # Solicita a quantidade de parcelas ao usuário
    preco = preco_normal + (preco_normal * 0.2) # Calcula o preço final, incluindo 20% de juros
    valor_parcela = preco / parcelas # Calcula o valor da parcela
    print (f'Sua compra será parcelada em {parcelas}x de R${valor_parcela:.2f} com juros.') # Imprime o resultado da compra parcelada com juros
else: # Caso seja digitada uma opção inválida
    preco = 0
    print("Condição de pagamento inválida.")

# Por fim, apresentamos o preço a ser pago ao usuário
print(f"Sua compra de R${preco_normal} vai custar R${preco:.2f} no final.")