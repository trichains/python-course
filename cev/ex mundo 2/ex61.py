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
