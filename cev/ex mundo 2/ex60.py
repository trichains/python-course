# Este código solicita que o usuário digite um valor, calcula o fatorial desse valor e imprime o resultado na tela. O fatorial é calculado usando um loop while que multiplica o valor atual do fatorial pelo valor atual do número até que o número seja reduzido a 1.

valor = int(input('Digite um número para calcular seu Fatorial: '))  # Solicita que o usuário digite um valor e armazena na variável "valor",   convertendo para um número inteiro com a função "int"
fatorial = 1  # Atribui o valor 1 à variável "fatorial"

print(f'{valor}! = ', end='')  # Imprime o valor da variável "valor", seguido de um ponto de exclamação (fatorial).

while valor > 0:  # Inicia um loop while que executa enquanto "valor" for maior que 0
    
    print(valor,end='')  # Imprime o valor atual da variável "valor", sem adicionar um caractere de fim de linha
    print(' x ' if valor > 1 else ' = ', end='')  # Imprime a string ' x ' se o valor da variável "valor" for maior do que 1, caso contrário imprime a string ' = ', sem adicionar um caractere de fim de linha

    fatorial *= valor  # Multiplica o valor atual da variável "fatorial" pelo valor atual da variável "valor" e armazena o resultado em "fatorial"
    valor -= 1  # Decrementa o valor da variável "valor" em 1 a cada iteração do loop

print(fatorial)  # Imprime na tela o valor final do fatorial armazenado na variável "fatorial"