from datetime import date  # importa o módulo date da biblioteca datetime

hoje = date.today()  # obtém a data atual
maior_idade = 0  # inicializa o contador de pessoas que atingiram a maioridade
menor_idade = 0  # inicializa o contador de pessoas que ainda não atingiram a maioridade

for i in range(1, 8):  # loop de 1 a 7 (para 7 pessoas)
    ano = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))  # solicita o ano de nascimento da pessoa i
    idade = hoje.year - ano  # calcula a idade da pessoa i

    if idade >= 18:  # se a idade for maior ou igual a 18
        maior_idade += 1  # incrementa o contador de pessoas que atingiram a maioridade
    else:  # senão
        menor_idade += 1  # incrementa o contador de pessoas que ainda não atingiram a maioridade

print(f'{maior_idade} pessoas já atingiram a maioridade.')  # exibe o número de pessoas que atingiram a maioridade
print(f'{menor_idade} pessoas ainda não atingiram a maioridade.')  # exibe o número de pessoas que ainda não atingiram a maioridade
