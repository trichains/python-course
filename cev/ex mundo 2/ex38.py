entrada_primeiro_valor = int ( input ( " Digite o primeiro valor: " ))
entrada_segundo_valor = int ( input ( " Digite o segundo valor: " ))

if entrada_primeiro_valor > entrada_segundo_valor:
    print(f'O primeiro valor "{entrada_primeiro_valor}" é maior que o segundo valor "{entrada_segundo_valor}"')
elif entrada_segundo_valor > entrada_primeiro_valor:
    print(f'O segundo valor "{entrada_segundo_valor}" é maior que o primeiro valor "{entrada_primeiro_valor}"')
else:
    print(f'Não existe valor maior, os dois são iguais.')