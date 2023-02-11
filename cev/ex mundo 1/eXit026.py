#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A” 
#em que posição ela aparece a primeira vez.
#em que posição ela aparece a última vez.
f=str(input('Digite uma frase qualquer: ')).lower().strip()
print(f'a letra A aparece {f.count("a")} vezes.\na primeira letra A apareceu na posição:{f.find("a")+1}\na ultima letra A aparece na posição:{f.rfind("a")+1}')