# captura o primeiro termo da progressão aritmética
a1 = int(input("Digite o primeiro termo: "))

# captura a razão da progressão aritmética
r = int(input("Digite a razão: "))

# imprime o título da sequência
print("Os 10 primeiros termos da progressão são:", end=' ')

# loop para imprimir os 10 primeiros termos da sequência
for i in range(1, 11):
    # calcula o i-ésimo termo da sequência
    termo = a1 + (i - 1) * r
    
    # imprime o i-ésimo termo da sequência
    print(termo, end=' ')
