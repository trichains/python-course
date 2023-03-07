# Criando a tupla 'produtos' com as informações dos itens e seus respectivos preços
produtos = ('Gabinete: Ninja Hades', 151.90, 'Fonte: Redragon 500w', 269.90, 
            'Kit Xeon', 489.86, 'Placa de vídeo: Radeon RX 580 8GB', 496.86, 
            'Armazenamento: Xraydisk SSD 512GB NVMe', 127.47)

# Imprimindo o cabeçalho da listagem de preços
print(f"{'LISTAGEM DE PREÇOS':^50}")
print('-=-'*17)

# Looping sobre os itens e seus preços, e imprimindo-os na tela formatados com os preços alinhados à direita
for i in range(0, len(produtos), 2):
    print(f"{produtos[i]:.<40} R${produtos[i+1]:>8.2f}")

# Imprimindo uma linha de separação
print('-=-'*17)
