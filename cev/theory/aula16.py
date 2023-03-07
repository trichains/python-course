# TUPLAS

# Definindo a tupla "lanche"
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

# Percorrendo a tupla com um loop "for" e exibindo cada elemento
for comida in lanche:
    print(f'Comi {comida}')

# Percorrendo a tupla com um loop "for" usando o "range" para percorrer cada posição da tupla e exibindo cada elemento e a posição correspondente
for cont in range (0, len(lanche)):
    print(f'Comi {lanche[cont]} na posição {cont}')

# Percorrendo a tupla com um loop "for" usando a função "enumerate" para obter a posição de cada elemento e exibindo cada elemento e a posição correspondente
for pos, comida in enumerate(lanche):
    print(f'Comi {comida} na posição {pos}')

# O primeiro loop for percorre a tupla lanche e exibe cada elemento usando uma f-string para formatar a saída.

# O segundo loop for percorre a tupla usando a função range para gerar uma sequência de índices, que são usados para acessar cada elemento da tupla usando a sintaxe de indexação. A cada iteração do loop, um elemento é exibido juntamente com sua posição correspondente.

# O terceiro loop for é semelhante ao segundo, mas usa a função enumerate para obter o índice e o valor de cada elemento da tupla. Isso torna o código mais legível e elimina a necessidade de usar a função range. Em vez disso, a variável pos recebe o índice de cada elemento e a variável comida recebe o próprio elemento. A cada iteração do loop, um elemento é exibido juntamente com sua posição correspondente.