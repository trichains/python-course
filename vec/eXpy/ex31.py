distancia=float(input("Qual vai ser a distancia da viagem em Km?: "))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'O preço da sua passagem será de {preço:.2f}R$')
