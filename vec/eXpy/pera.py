numero= input('Digite um número inteiro de 0 a 9999. ')


#Apaga os espaços a fim de não considerá-los na contagem.
formatado=numero.replace(' ','')
#O programa aparece a mensagem erro caso o usuário ultrapasse os 4 algarismos.
if len(formatado) > 4:
    print('Erro. Só são permitidos números de 4 algarismos')
else:
    if len(formatado)==4:
        print('Milhar: {}'.format(formatado[0]))
        print('Centena: {}'.format(formatado[1]))
        print('Dezena: {}'.format(formatado[2]))
        print('Unidade: {}'.format(formatado[3]))
    if len(formatado)==3:
        print('Centena: {}'.format(formatado[0]))
        print('Dezena: {}'.format(formatado[1]))
        print('Unidade: {}'.format(formatado[2]))
    if len(formatado)==2:
        print('Dezena: {}'.format(formatado[0]))
        print('Unidade: {}'.format(formatado[1]))
    if len(formatado)==1:
        print('Unidade: {}'.format(formatado[0]))