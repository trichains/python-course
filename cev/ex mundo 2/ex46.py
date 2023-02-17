# Importando a biblioteca time, que permite controlar o fluxo do programa com base no tempo
from time import sleep

# Importando a biblioteca emoji, que permite usar emojis no output do programa
from emoji import emojize

# Iniciando um loop que vai contar de 10 até 0 (exclusivo), com decremento de -1
for i in range (10,-1,-1):
    
    # Imprimindo o valor atual da variável i
    print(i)
    
    # Pausando a execução do programa por 1 segundo
    sleep(1)

# Quando o loop terminar, imprimir um emoji de festa
print(emojize(':party_popper:'))
