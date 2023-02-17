# Inicializa as variáveis 'maior_peso' e 'menor_peso' com o valor da primeira pessoa informada pelo usuário
maior_peso = menor_peso = float(input('Qual o peso da 1ª pessoa? (kg): '))

# Loop para capturar os pesos das outras quatro pessoas informadas pelo usuário
for i in range(2, 6):
    peso = float(input(f'Qual o peso da {i}ª pessoa? (kg): '))
    
    # Verifica se o peso capturado é maior do que o maior peso já capturado
    if peso > maior_peso:
        maior_peso = peso
    # Verifica se o peso capturado é menor do que o menor peso já capturado
    elif peso < menor_peso:
        menor_peso = peso

# Imprime o maior e menor peso capturados
print(f'O maior peso lido foi: {maior_peso:.2f} kg')
print(f'O menor peso lido foi: {menor_peso:.2f} kg')
