# Primeiro, solicitamos ao usuário que informe o preço normal do produto
preco_normal = float(input("Informe o preço normal do produto: "))

# Em seguida, apresentamos as opções de pagamento ao usuário
print ("|"," "*2,"CONDIÇÕES DE PAGAMENTO" + " "*2,"|")
print ("| [1] À vista dinheiro/cheque |")
print ("| [2] À vista no cartão " + " "*5,"|")
print ("| [3] Em até 2x no cartão " + " "*3,"|")
print ("| [4] 3x ou mais no cartão " + " "*2,"|")

# Depois, solicitamos ao usuário a escolha da condição de pagamento
condicao = int(input("Digite a condição do valor: "))

# Verificamos a condição escolhida e calculamos o preço a ser pago
if condicao == 1: # Será acrescentado 10% de desconto
    preco = preco_normal - (preco_normal * 0.1)
elif condicao == 2: # Será acrescentado 5% de desconto
    preco = preco_normal - (preco_normal * 0.05)
elif condicao == 3: # Sem desconto ou juros
    preco = preco_normal
elif condicao == 4: # Será acrescentado 20% de juros
    preco = preco_normal + (preco_normal * 0.2)
else: # Caso seja digitada uma opção inválida
    preco = 0
    print("Condição de pagamento inválida.")

# Por fim, apresentamos o preço a ser pago ao usuário
print(f"O preço a ser pago é de {preco:.2f}")