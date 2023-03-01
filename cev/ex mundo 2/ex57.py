# Inicializa a variável "sexo" com uma string vazia
sexo = ''

# Entra em um laço enquanto o valor de "sexo" não for 'M' e não for 'F'
while sexo != 'M' and sexo != 'F':
    # Pede ao usuário para digitar o sexo da pessoa remove espaços em branco, converte para maiúsculas e extrai o primeiro caractere.
    sexo = input('Qual o sexo da pessoa?: (M/F): ').strip().upper()[0]
    
    # Verifica se o valor de "sexo" é inválido e exibe uma mensagem de erro caso seja
    if sexo != 'M' and sexo != 'F':
        print('\033[31mValor inválido. Digite apenas M ou F.\033[m')

# Verifica se o valor de "sexo" é 'M' e exibe uma mensagem correspondente
if sexo == 'M':
    print('O sexo da pessoa é masculino.')
# Caso contrário, exibe uma mensagem correspondente a 'F'
else:
    print('O sexo da pessoa é feminino.')
