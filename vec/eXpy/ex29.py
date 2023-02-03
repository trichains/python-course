# Valor da multa R$7,00 por cada Km acima da velocidade máxima permitida "80"
print("-=-"*20,"\nO VALOR DA MULTA É DE R$7,00 POR CADA KM ACIMA DA VELOCIDADE PERMITIDA!")
print("VELOCIDADE MÁXIMA PERMITIDA ~> 80Km/h")
print("-=-"*20)
velocidade = int(input("O veículo está em que velocidade?: Km/h ")) # Vai ler a velocidade em Km/h do veículo.
permitida = 80 # Essa váriavel recebe a velocidade máxima permitida que neste caso é 80Km/h.
multa = (velocidade - permitida)*7 # Recebe a velocidade do veículo digitada pelo usuario subtraindo pela velocidade máxima permitida, por fim, multiplica o resultado pelo valor da multa.
if velocidade > permitida: # Se o valor digitado for maior que a velocidade máxima permitida então:
    print(f'O veículo está acima da velocidade permitida "{velocidade}Km/h".\nO dono do veículo terá de pagar uma multa avaliada em: R${multa}.')
else:
    print("O veículo está dentro da velocidade permitida.")