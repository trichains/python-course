# Início do bloco try-except para tratar exceções
try:
    # Captura de entrada do usuário e conversão para inteiro
    n1 = int(input('Digite um número: '))
    
    # Impressão do título da tabuada
    print(f'TABUADA DO {n1}')
    
    # Loop para imprimir cada linha da tabuada
    for i in range (1, 11):
        # Impressão da linha atual da tabuada
        print(f'{n1} x {i} = {n1*i}')
        
# Captura da exceção gerada caso o valor inserido não seja um número inteiro válido
except ValueError:
    # Impressão de mensagem de erro
    print('Erro: você precisa digitar um número inteiro válido')
