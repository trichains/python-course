# inicializa as variáveis de contagem
soma_idades = 0
maior_idade_homem = 0
nome_homem_mais_velho = ""
num_mulheres_menos_20 = 0

# faz um loop para ler as informações de cada pessoa
for i in range(1, 5):
    print(f"Digite os dados da {i}ª pessoa:")
    nome = input("Nome: ").lower()
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()

    # atualiza a soma das idades
    soma_idades += idade

    # verifica se a pessoa é homem e tem a maior idade até o momento
    if sexo == "M" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome

    # verifica se a pessoa é mulher e tem menos de 20 anos
    if sexo == "F" and idade < 20:
        num_mulheres_menos_20 += 1

# calcula a média de idade do grupo
media_idades = soma_idades / 4

# exibe as informações solicitadas
print(f"Média de idade do grupo: {media_idades:.1f}")
print(f"Nome do homem mais velho: {nome_homem_mais_velho}")
print(f"Mulheres com menos de 20 anos: {num_mulheres_menos_20}")
