frase = input("Digite uma palavra ou frase: ")

# Remova espaços da frase e converta para minúsculas
frase = frase.replace(' ', '').lower()

# Inverta a ordem dos caracteres na frase
frase_invertida = frase[::-1]

# Compare a frase original com a frase invertida
if frase == frase_invertida:
    print("A palavra/frase é um palíndromo!")
else:
    print("A palavra/frase não é um palíndromo.")
