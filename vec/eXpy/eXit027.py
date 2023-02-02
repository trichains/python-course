#Faça um programa que leia o nome completo de uma pessoa
#mostrando em seguida o primeiro e o último nome separadamente.
n=str(input('Digite seu nome completo?: ')).strip()
print(f'Seu nome completo é: {n}\nSeu primeiro nome é: {n.split()[0]}\nSeu último nome é: {n.split()[len(n.split())-1]}')