n = int(input('Digite o número de termos da sequência de Fibonacci que você deseja ver: '))

# Definir os primeiros dois números da sequência
a, b = 0, 1

# Imprimir os primeiros dois termos
print(a, end=' ')
print(b, end=' ')

# Calcular e imprimir os próximos n-2 termos da sequência
count = 2  # contador iniciado em 2 porque já imprimimos os dois primeiros termos
while count < n:
    c = a + b  # calcular o próximo termo
    print(c, end=' ')  # imprimir o próximo termo
    a, b = b, c  # atualizar a e b para calcular o próximo termo
    count += 1  # incrementar o contador
