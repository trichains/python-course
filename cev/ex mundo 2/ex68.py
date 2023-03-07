from random import randint

vitorias = 0

while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    while True:
        poui = input('Par ou Impar? [P/I]: ').strip().upper()[0]
        if poui in ['P','I']:
            break
        else:
            print('Digite apenas P para PAR ou I para IMPAR.')
    soma = jogador + computador

    if soma % 2 == 0 and poui == 'P':
        print(f'Você jogou {jogador} e o computador jogou {computador}.\n'
              f'A soma foi {soma} então o resultado é PAR\n'
              f'Você ganhou!')
        vitorias += 1
    elif soma % 2 == 1 and poui == 'I':
        print(f'Você jogou {jogador} e o computador jogou {computador}.\n'
              f'A soma foi {soma} então o resultado é IMPAR\n'
              f'Você ganhou!')
        vitorias += 1
    else:
        print(f'Você jogou {jogador} e o computador jogou {computador}.\n'
              f'A soma foi {soma} então o resultado é {"PAR" if soma % 2 == 0 else "IMPAR"}\n'
              f'Você perdeu!')
        break

print(f'Você venceu {vitorias} vezes.')
