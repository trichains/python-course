# definindo a variável "soma" como 0
soma = 0
# definindo a variável "cont" como 0
cont = 0

# iterando através de todos os números ímpares de 1 a 500 com um passo de 2
for i in range(1, 501, 2):
    # verificando se o número atual é divisível por 3
    if i % 3 == 0:
        # incrementando o contador "cont" por 1
        cont += 1
        # adicionando o número atual à variável "soma"
        soma += i

# imprimindo o resultado
print(f"A soma de todos os {cont} números ímpares de 0 a 500 que são divisíveis por 3 é:", soma)
