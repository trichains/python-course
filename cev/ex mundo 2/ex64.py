# Inicializa as variáveis num, soma e count com valor 0
num = soma = count = 0
# Enquanto o valor de num for diferente de 999, o bloco de código dentro do laço será executado
while num != 999:
    # Solicita ao usuário que digite um número inteiro e converte o valor para inteiro
    num = int(input('Digite um número inteiro [999 para parar]: '))
    # Adiciona 1 ao contador de números digitados
    count += 1
    # Se o valor de num for diferente de 999, adiciona o valor de num à variável soma
    if num != 999:
        soma += num 

    # Se o valor de num for igual 999, subtrai 1 ao contador de números digitados
    if num == 999:
        count -= 1

# Quando o valor de num for igual a 999, o laço termina e o bloco de código abaixo é executado
# Imprime a quantidade de números digitados e a soma dos valores (desconsiderando o 999)
print(f'Foram digitados {count} números.\n'
    f'A soma entre os valores (desconsiderando o 999) é: {soma}')
