# Importa a função randint da biblioteca random
from random import randint

# Cria uma tupla com 5 números inteiros aleatórios entre 1 e 10
numeros = tuple(randint(1, 10) for i in range(5))

# Imprime a tupla de números aleatórios na tela
print("Tupla de números aleatórios:", numeros)

# Encontra o maior valor da tupla usando a função max() e atribui à variável maior
maior = max(numeros)

# Encontra o menor valor da tupla usando a função min() e atribui à variável menor
menor = min(numeros)

# Imprime o maior valor encontrado na tupla na tela
print("Maior valor:", maior)

# Imprime o menor valor encontrado na tupla na tela
print("Menor valor:", menor)
