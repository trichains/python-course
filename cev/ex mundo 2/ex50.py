# Inicialização das variáveis soma e contador com valor zero
soma = 0
cont = 0

# Loop para receber entrada do usuário e identificar números pares
for i in range (1,7):
    # Captura de entrada do usuário como inteiro
    inteiros = int(input(f'Digite o {i}º valor: '))
    
    # Verifica se o número é par
    if inteiros % 2 == 0:
        # Incrementa a soma dos números pares
        soma += inteiros
        # Incrementa o contador de números pares
        cont += 1

# Impressão do resultado final
print(f"Você informou {cont} números pares e a soma foi: {soma}")
