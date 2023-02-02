n=str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print(f'Todas as letras Maiusculas: {n.upper()}\nTodas as letras Minusculas: {n.lower()}\nseu nome {n} possui {len(n)-n.count(" ")} letras ao todo\nSeu primeiro nome tem {n.find(" ")} letras.')