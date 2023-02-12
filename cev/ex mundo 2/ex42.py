# Imprime o título do programa
print("-=-"*8,"\nANALISADOR DE TRIÂNGULOS\n" + "-=-"*8)

# Recebe o comprimento dos lados
print("Informe os comprimentos dos lados: ")
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

# Verifica se os lados informados formam ou não um triângulo
if (a >= b + c) or (b >= a + c) or (c >= a + b):
    print("Os segmentos acima NÃO PODEM formar um triângulo!.")
else:
    print("Os segmentos acima FORMAM um triângulo!.")

# Verifica se os lados informados formam um triângulo equilátero, isósceles ou escaleno
if (a == b == c):
    print("Os segmentos acima formam um triângulo EQUILÁTERO!.")
elif (a == b) or (b == c) or (a == c):
    print("Os segmentos acima formam um triângulo ISÓSCELES!.")
else:
    print("Os segmentos acima formam um triângulo ESCALENO!.")
