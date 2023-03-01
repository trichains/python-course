# leitura do primeiro termo e da razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# inicialização do contador e do número de termos a serem exibidos
contador = 1
numero_de_termos = 10

# exibição dos termos da PA usando um loop while
while contador <= numero_de_termos:
    termo_atual = primeiro_termo + (contador - 1) * razao
    print(termo_atual)
    contador += 1
    
# perguntar ao usuário se ele deseja exibir mais alguns termos
mais_termos = input("Deseja exibir mais alguns termos?\nDigite a quantidade ou 0 para encerrar: ")
mais_termos = int(mais_termos)

# loop aninhado para exibir mais termos
while mais_termos != 0:
    for i in range(contador, contador + mais_termos):
        termo_atual = primeiro_termo + (i - 1) * razao
        print(termo_atual)
        
    contador += mais_termos
    
    # perguntar novamente ao usuário se ele deseja exibir mais termos
    mais_termos = input("Deseja exibir mais alguns termos?\nDigite a quantidade ou 0 para encerrar: ")
    mais_termos = int(mais_termos)
