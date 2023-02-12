# importa a função "choice" da biblioteca random
from random import choice

# imprime o título do jogo e o aviso para o usuário escolher a jogada
print("Jokenpô\nEscolha sua jogada: pedra, papel ou tesoura")

# lê a jogada do usuário e a armazena como string, convertendo para letra minúscula
jogada_usuario = input().lower()

# cria uma lista com as possíveis jogadas
jogadas = ["pedra","papel","tesoura"]

# escolhe a jogada do computador de forma aleatória
jogada_computador = choice(jogadas)

# compara a jogada do usuário com a do computador
# se as jogadas forem iguais, imprime "EMPATE"
if jogada_usuario == jogada_computador:
    print("EMPATE")
# se a jogada do usuário for "pedra" e a do computador for "tesoura", imprime "VOCÊ VENCEU!"
elif jogada_usuario == "pedra" and jogada_computador == "tesoura":
    print("Jogador [\U0001f44a] x [\u270c] Computador")
    print("VOCÊ VENCEU!")
# se a jogada do usuário for "tesoura" e a do computador for "papel", imprime "VOCÊ VENCEU!"
elif jogada_usuario == "tesoura" and jogada_computador == "papel":
    print("Jogador [\u270c] x [\U0000270b] Computador")
    print("VOCÊ VENCEU!")
# se a jogada do usuário for "papel" e a do computador for "pedra", imprime "VOCÊ VENCEU!"
elif jogada_usuario == "papel" and jogada_computador == "pedra":
    print("Jogador [\U0000270b] x [\U0001f44a] Computador")
    print("VOCÊ VENCEU!")
    
# caso contrário, o computador venceu
else:
    # verifica a jogada do computador e imprime o emoji correspondente
    if jogada_computador == "pedra":
        print("Jogador [\u270c] x [\U0001f44a] Computador")
    elif jogada_computador == "tesoura":
        print("Jogador [\U0000270b] x [\u270c] Computador")
    elif jogada_computador == "papel":
        print("Jogador [\U0001f44a] x [\U0000270b] Computador")
    # imprime "O COMPUTADOR VENCEU!"
    print("O COMPUTADOR VENCEU!")
