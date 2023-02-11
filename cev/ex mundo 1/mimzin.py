n1= float (input("Nota de caderno é: ")) 
n2= float (input ('Nota da Prova Mensal: '))
n3= float (input ('Nota da Prova Bimestral: '))

nf= (n1+n2*2+n3*3)/6

if nf >= 6.0:
    print (f"Aprovado! Sua nota é {nf:.2f}.")
else:
    print (f"REPROVADO! Sua nota é {nf:.2f}.")