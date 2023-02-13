# Solicita ao usuário que digite um número inteiro
entrada_numero = int(input("Digite um número inteiro: "))

# Exibe as opções de base para a conversão
print('''Qual será a base da conversão?
[1] para binário
[2] para octal
[3] para hexadecimal''')

# Solicita ao usuário a escolha da base para a conversão
entrada_escolha = int(input(" Sua opção: "))

# Verifica a escolha do usuário e realiza a conversão
if entrada_escolha == 1:
    # Converte o número para binário e remove o prefixo '0b'
    print(f'O número {entrada_numero} em binário é: {bin(entrada_numero)[2:]}')
elif entrada_escolha == 2:
    # Converte o número para octal e remove o prefixo '0o'
    print(f'O número {entrada_numero} em octal é: {oct(entrada_numero)[2:]}')
elif entrada_escolha == 3:
    # Converte o número para hexadecimal e remove o prefixo '0x'
    print(f'O número {entrada_numero} em hexadecimal é: {hex(entrada_numero)[2:]}')
else:
    # Mensagem de erro caso digite uma opção inválida
    print('Opção inválida.')
