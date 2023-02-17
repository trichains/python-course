num = int(input("Digite um número inteiro: ")) # solicita ao usuário um número inteiro e armazena na variável 'num'

if num > 1: # verifica se o número informado é maior do que 1 e, se for:
    for i in range(2, num): # percorre todos os números de 2 até o valor informado pelo usuário - 1
        if (num % i) == 0: # verifica se o número informado é divisível pelo número atual do laço 'for'
            print(num, "não é um número primo") # caso seja divisível, imprime a mensagem informando que o número não é primo
            break # sai do laço 'for'
    else: # caso o laço 'for' seja percorrido completamente sem encontrar nenhum número que divida o número informado
        print(num, "é um número primo") # o número é primo e o programa imprime a mensagem informando isso
else: # caso o número informado seja menor ou igual a 1
    print(num, "não é um número primo") # não é um número primo e o programa imprime a mensagem informando isso
