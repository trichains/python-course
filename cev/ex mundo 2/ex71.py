# Solicita ao usuário o valor a ser sacado
valor = int(input("Digite o valor a ser sacado: R$"))

# Lista com os valores das notas disponíveis
notas = [50, 20, 10, 1]

# Itera sobre as notas disponíveis
for nota in notas:
    # Inicializa a quantidade de notas a serem entregues
    qtd_notas = 0
    
    # Enquanto o valor a ser sacado for maior ou igual ao valor da nota atual, continua subtraindo o valor da nota do valor a ser sacado e incrementando a quantidade de notas a serem entregues
    while valor >= nota:
        valor -= nota
        qtd_notas += 1
    
    # Se a quantidade de notas a serem entregues for maior do que zero, exibe a quantidade na tela
    if qtd_notas > 0:
        print(f"Total de {qtd_notas} cédulas de R${nota}")
