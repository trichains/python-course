maior_peso = menor_peso = float(input('Qual o peso da 1ª pessoa? (kg): '))

for i in range(2, 6):
    peso = float(input(f'Qual o peso da {i}ª pessoa? (kg): '))
    if peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso

print(f'O maior peso lido foi: {maior_peso:.2f} kg')
print(f'O menor peso lido foi: {menor_peso:.2f} kg')
