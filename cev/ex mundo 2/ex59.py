try:
    # Solicita ao usuário que insira dois valores e define as variáveis valor_1 e valor_2
    valor_1 = int(input('Digite o primeiro valor: '))
    valor_2 = int(input('Digite o segundo valor: '))
    
    # Define as variáveis escolha e continuar
    escolha = 0
    continuar = ''

    # Enquanto a opção escolhida for diferente de 5, apresenta as opções e solicita a escolha do usuário
    while escolha != 5:
        # Apresenta as opções para o usuário
        print('Escolha uma opção\n'
              '[1] somar\n'
              '[2] multiplicar\n'
              '[3] maior número\n'
              '[4] novos números\n'
              '[5] sair do programa.\n')
        try:
            # Solicita que o usuário escolha uma opção e define a variável escolha com a opção escolhida
            escolha = int(input('Qual opção?: '))

            # Realiza a ação correspondente à opção escolhida
            if escolha == 1:
                soma = (valor_1 + valor_2)
                print(f'A soma de {valor_1} com {valor_2} é igual a: {soma}')
            elif escolha == 2:
                multiplicador = (valor_1 * valor_2)
                print(f'A multiplicação de {valor_1} com {valor_2} é igual a: {multiplicador}')
            elif escolha == 3:
                if valor_1 > valor_2:
                    print(f'O maior número digitado foi: {valor_1}')
                else:
                    print(f'O maior número digitado foi: {valor_2}')
            elif escolha == 4:
                valor_1 = int(input('Digite o primeiro valor: '))
                valor_2 = int(input('Digite o segundo valor: '))
            elif escolha == 5:
                print('Saindo do programa...')
            else:
                print('Opção inválida. Tente novamente.')

            # Se a escolha for diferente de 5, pergunta se o usuário quer continuar e valida a entrada do usuário
            if escolha != 5:
                continuar = input('Quer continuar? (S/N): ').upper()
                while continuar not in ('S', 'N'):
                    print('Opção inválida. Tente novamente.')
                    continuar = input('Quer continuar? (S/N): ').upper()
        # Se o usuário inserir um valor que não pode ser convertido para inteiro, apresenta uma mensagem de erro
        except ValueError:
            print('Erro! Digite apenas números inteiros.')
    
    # Ao sair do loop, apresenta uma mensagem de agradecimento
    print('Obrigado por usar o programa!')
    
except ValueError:
    print('Erro! Digite apenas números inteiros.')
