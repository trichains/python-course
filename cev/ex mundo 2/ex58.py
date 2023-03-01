from random import randrange
from time import sleep

# Gera um número aleatório entre 0 e 10.
numero = randrange(0, 11)

# Inicia a variável palpite com uma string vazia e a variável tentativas com zero.
palpite = ''
tentativas = 0

# Imprime a mensagem de início do jogo.
print('🤔🤔🤔 Vou pensar em um número entre 0 e 10, tente adivinhar qual é. 🤔🤔🤔')

# Enquanto o palpite do usuário for diferente do número gerado aleatoriamente:
while palpite != numero:
    try:
        # Solicita um palpite do usuário como um número inteiro.
        palpite = int(input('🤔🤔🤔 Que número estou pensando?: '))
    except ValueError:
        # Se o usuário inserir um valor inválido, imprime uma mensagem de erro e continua a execução do loop.
        print('❌❌❌ Oops! Você precisa inserir um número válido. ❌❌❌')
        continue
    
    # Imprime uma mensagem de "processando" para dar feedback ao usuário.
    print('⏳⏳⏳ PROCESSANDO...')
    # Espera 1 segundo antes de continuar a execução.
    sleep(1)
    if palpite != numero:
        # Se o palpite estiver incorreto, imprime uma mensagem de erro e aumenta a contagem de tentativas.
        print('❌❌❌ Errou!, tente novamente! ❌❌❌')
        tentativas += 1

# Quando o palpite estiver correto, imprime uma mensagem de sucesso e o número de tentativas.
print(f'🎉🎉🎉 Parabéns! você acertou, eu pensei no número {numero}! 🎉🎉🎉')
print(f'👏👏👏 Ao todo houveram {tentativas} tentativas até acertar. 👏👏👏')
