# Criação de uma tupla contendo os times do Brasileirão
brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 
               'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 
               'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 
               'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atletico-GO', 
               'Avaí', 'Juventude')

# Imprime uma linha de separação
print('-=-'*15)

# Imprime a lista de times do Brasileirão
print(f'Lista de Times do Brasileirão: {brasileirao}')
print('-=-'*15)

# Imprime os 5 primeiros colocados da lista
print(f'Os 5 primeiros colocados são: {brasileirao[:5]}')
print('-=-'*15)

# Imprime os 4 últimos colocados da lista
print(f'Os 4 últimos colocados são: {brasileirao[-4:]}')
print('-=-'*15)

# Imprime a lista de times em ordem alfabética
print(f'Lista dos times em ordem alfabética: {sorted(brasileirao)}')
print('-=-'*15)

# Imprime a posição do Flamengo na lista
print(f'Flamengo está na {brasileirao.index("Flamengo")+1}ª posição.')
print('-=-'*15)
