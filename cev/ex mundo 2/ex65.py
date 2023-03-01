# Inicializa as variáveis
cont = soma = 0
maior = float('-inf')
menor = float('inf')

# Loop para leitura dos números
continuar = 'S'
while continuar == 'S':
    num = int(input('Digite um número inteiro: '))
    cont += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    continuar = input('Quer continuar? (S/N): ').upper()

# Calcula a média
media = soma / cont

# Exibe os resultados
print(f'Média: {media:.2f}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
