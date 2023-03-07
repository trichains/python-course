# inicializa as variáveis de contagem
maior_18 = 0  # quantidade de pessoas com mais de 18 anos
homem = 0  # quantidade de homens cadastrados
menos_20 = 0  # quantidade de mulheres com menos de 20 anos

# loop principal do programa
while True:
    # pede a idade da pessoa
    idade = int(input('Qual a idade da pessoa?: '))
    
    # loop para garantir que o sexo informado seja válido (M ou F)
    while True:
        sexo = input('Qual o sexo da pessoa?\nDigite [M] para masculino ou [F] para feminino: ').strip().upper()[0]
        if sexo == 'M' or sexo == 'F':
            break
            
    # verifica se a pessoa é mulher com menos de 20 anos
    if sexo == 'F' and idade < 20:
        menos_20 += 1
        
    # verifica se a pessoa é homem
    if sexo == 'M':
        homem += 1
        
    # verifica se a pessoa tem mais de 18 anos
    if idade > 18:
        maior_18 += 1
        
    # loop para perguntar se deseja continuar ou encerrar o programa
    while True:
        continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        print('Obrigado!')
        break

# exibe as informações finais do programa
print(f'AO TODO:\n'
      f'{maior_18} pessoas tem mais de 18 anos.\n'
      f'Foram cadastrados {homem} homens.\n'
      f'{menos_20} mulheres tem menos de 20 anos.')
