nome=str(input('Digite seu nome: '))
if nome == 'Cristhian':
    print("Que nome bonito!")
elif nome == 'João' or nome == 'Maria':
    print('Seu nome é bem comum no Brasil')
elif nome in ('Bruna Ana Cláudia Fernanda Beatriz'):
    print('Belo nome feminino!')
else:
    print('Que nome sem graça... :/')
print(f'Seja bem vindo(a)! {nome}!')