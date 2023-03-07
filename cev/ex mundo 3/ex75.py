# Lê 4 valores inteiros do teclado e armazena-os em uma tupla
valores = tuple(int(input("Digite um valor: ")) for i in range(4))

# Encontra a posição do primeiro valor 3 na tupla, se estiver presente
if 3 in valores:
    posicao = valores.index(3) + 1
    print("O primeiro valor 3 foi digitado na posição", posicao)
else:
    print("O valor 3 não foi digitado na tupla.")

# Cria uma tupla apenas com os números pares
pares = tuple(valor for valor in valores if valor % 2 == 0)

# Imprime a tupla na tela
print("Valores digitados:", valores)

# Conta quantas vezes o valor 9 aparece na tupla e imprime o resultado na tela
print(f"O valor 9 apareceu {valores.count(9)} vezes na tupla.")

# Imprime o resultado na tela, apenas se a tupla não estiver vazia
if pares:
    print("Os números pares digitados foram:", pares)
else:
    print("Nenhum número par foi digitado.")
