# Lê os dois valores informados pelo usuário
primeiro_valor = int(input("Informe o primeiro valor: "))
segundo_valor = int(input("Informe o segundo valor: "))

# Verifica qual dos dois valores é o maior
if primeiro_valor > segundo_valor:
    # Imprime o resultado, indicando que o primeiro valor é o maior
    print(f"\033[32mO primeiro valor '{primeiro_valor}' é maior que o segundo valor '{segundo_valor}'\033[0m")
elif segundo_valor > primeiro_valor:
    # Imprime o resultado, indicando que o segundo valor é o maior
    print(f"\033[33mO segundo valor '{segundo_valor}' é maior que o primeiro valor '{primeiro_valor}'\033[0m")
else:
    # Imprime o resultado, indicando que não existe um valor maior, pois os dois são iguais
    print(f'\033[31mNão existe valor maior, os dois são iguais.\033[0m')
