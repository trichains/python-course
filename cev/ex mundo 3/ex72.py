# Define uma tupla com as palavras correspondentes aos números de 0 a 20
extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Solicita ao usuário um número entre 0 e 20
numero = int(input('Digite um número entre 0 e 20: '))

# Executa um loop até que o usuário digite um número válido
while True:
    if numero > 20 or numero < 0:
        numero = int(input('Digite apenas um número entre 0 e 20: '))
    else:
        break

# Imprime a palavra correspondente ao número digitado pelo usuário
print(f'Você digitou o número {extenso[numero]}')
