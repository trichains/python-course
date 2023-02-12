entrada_numero = int(input('Digite um número inteiro: '))

print('Qual será a base da conversão?\n[1] para binário\n[2] para octal\n[3] para hexadecimal')

entrada_escolha = int(input('Qual sua escolha: '))

if entrada_escolha == 1:
    resultado = bin(entrada_numero)[2:]
    print(f'O número {entrada_numero} em binário é: {resultado}')
elif entrada_escolha == 2:
    resultado = oct(entrada_numero)[2:]
    print(f'O número {entrada_numero} em octal é: {resultado}')
elif entrada_escolha == 3:
    resultado = hex(entrada_numero)[2:]
    print(f'O número {entrada_numero} em hexadecimal é: {resultado}')
else:
    print('Opção inválida.')