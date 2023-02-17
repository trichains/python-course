# Cria uma lista vazia chamada "numeros"
numeros = []

# Loop for que itera de 2 até 50, com incrementos de 2 em 2
for i in range(2, 51, 2):
    # Adiciona o número atual da iteração à lista "numeros"
    numeros.append(i)

# Imprime uma mensagem na tela mostrando a lista "numeros" contendo todos os números pares encontrados
print(f"Os números pares entre 1 e 50 são: {numeros}")
