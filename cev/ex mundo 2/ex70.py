total = 0                           # Inicializa a variável que irá armazenar o total gasto na compra
nome_barato = ''                    # Inicializa a variável que irá armazenar o nome do produto mais barato
barato = 0                          # Inicializa a variável que irá armazenar o preço do produto mais barato
produtos_mais_1000 = 0              # Inicializa a variável que irá armazenar a quantidade de produtos com preço acima de R$1000

while True:                         # Inicia o loop para a leitura dos produtos
    nome_produto = input('Qual o nome do produto?: ')    # Lê o nome do produto
    while True:                     # Inicia um loop para garantir que o preço digitado seja um número
        try:
            preco_produto = float(input('Qual o preço do produto?: R$'))
            break
        except ValueError:
            print('Valor inválido. Digite apenas números.')

    total += preco_produto          # Adiciona o preço do produto ao total gasto na compra
    if barato == 0 or preco_produto < barato:    # Verifica se o produto é o mais barato até o momento
        barato = preco_produto      # Atualiza o preço do produto mais barato
        nome_barato = nome_produto  # Atualiza o nome do produto mais barato

    if preco_produto > 1000:        # Verifica se o produto custa mais de R$1000
        produtos_mais_1000 += 1     # Incrementa a contagem de produtos com preço acima de R$1000

    while True:                     # Inicia um loop para garantir que a opção digitada seja S ou N
        continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
        if continuar in ['S', 'N']:
            break
        else:
            print('Opção inválida. Digite S ou N.')

    if continuar == 'N':            # Verifica se o usuário deseja parar de digitar produtos
        break

# Imprime o total gasto na compra e o produto mais barato
print(f'O total gasto na compra foi: {total:.2f}.\n'
      f'O produto mais barato é: {nome_barato} por R${barato:.2f}.')

# Imprime a quantidade de produtos com preço acima de R$1000
print(f'{produtos_mais_1000} produtos custam mais de R$1000.00')
