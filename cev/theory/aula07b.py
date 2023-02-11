n1=int(input('digite um valor: '))
n2=int(input('digite outro valor: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('a soma de {}\ncom {}\nvale {}'.format(n1,n2,s),end=' já ')
print('a multiplicação de {} com {} resulta em {}'.format(n1,n2,m),end=' portanto se ')
print('a divisão de {} com {} resultar em {:.3f}'.format(n1,n2,d),end=(' então '))
print('a divisão inteira resultaria {}'.format(di),end=(' uma vez que '))
print('sua exponenciação seja {}'.format(e))