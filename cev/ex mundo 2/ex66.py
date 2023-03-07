# Inicialização das variáveis de controle de contagem e soma
c = s = 0

# Loop infinito, que será interrompido pelo comando "break" quando o número 999 for informado
while True:
    # Leitura do número informado pelo usuário
    n = int(input('Digite um número inteiro [999 para parar]: '))
    
    # Verifica se o número informado é 999
    if n == 999:
        # se for, interrompe o loop infinito
        break
    
    # Incrementa a contagem de valores informados e realiza a soma acumulativa
    c += 1
    s += n

# Exibe o resultado final da contagem e soma dos valores informados
print(f'Foram digitados {c} números e a soma entre eles resulta em: {s}')
