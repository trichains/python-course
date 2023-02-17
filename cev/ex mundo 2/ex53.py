# Captura uma entrada de usuário como string, remove espaços extras no começo e no final, e converte todos os caracteres para maiúsculas.
frase = input("Digite uma palavra ou frase: ").strip().upper()

# Remova espaços da frase
junto = frase.replace(' ', '')

# Inverta a ordem dos caracteres na frase
frase_invertida = junto[::-1]

# Compare a frase original com a frase invertida
if junto == frase_invertida:
    print (f'O inverso de {frase} é {frase_invertida}')
    print("A palavra/frase é um palíndromo!")
else:
    print (f'O inverso de {frase} é {frase_invertida}')
    print("A palavra/frase não é um palíndromo.")
