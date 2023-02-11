from random import randrange #Importa a função randrange que randomiza os números
from time import sleep
r=randrange(0,5) #Faz o computador escolher um número de 0 a 5.
print("-=-"*20,"\nVou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-"*20)
n=int(input("Em que número eu pensei?: ")) # Jogador tenta adivinhar
print("PROCESSANDO...")
sleep(3)
if n == r:
    print(f"PARABÉNS, você me venceu!, eu pensei no número {n}")
else:
    print(f"GANHEI! Eu pensei no número {r} e não em {n}!")