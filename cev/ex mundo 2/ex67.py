# Loop infinito para exibição de tabuadas
while True:
    # Leitura do número informado pelo usuário
    tabuada = int(input('Quer ver a tabuada de qual valor?: '))

    # Verifica se o número digitado é negativo
    if tabuada < 0:
        # se for, encerra o loop infinito e exibe a mensagem de encerramento
        print('TABUADA ENCERRADA!\nVolte sempre!')
        break
    
    # Loop para exibição da tabuada do número informado
    for i in range(1, 11):
        print(f'{tabuada} x {i} = {tabuada*i}')
