from datetime import date

# Obtendo a data atual
hoje = date.today()

# Lendo o ano de nascimento
entrada_ano_nascimento = int(input("\033[36mInforme o seu ano de nascimento:\033[0m "))

# Lendo o sexo da pessoa
sexo = input("\033[36mInforme o seu sexo (masculino/feminino):\033[0m ")

# Calculando a idade
idade = hoje.year - entrada_ano_nascimento

# Verificando se a pessoa ainda não tem 18 anos
if idade < 18:
    # Se for do sexo masculino, deve se alistar
    if sexo.lower() == "masculino":
        print("\033[31mVocê ainda não tem\033[33m 18 anos.\033[31m\n"
        "Faltam\033[33m", 18 - idade ,"anos\033[31m para o seu \033[32malistamento militar.\033[0m"
        f"Você irá se alistar em {hoje.year + (18 - idade)}")
    # Se for do sexo feminino, não precisa se alistar
    else:
        print("\033[31mVocê ainda não tem\033[33m 18 anos.\033[31m\n"
        "\033[32m No entanto, como você é do sexo feminino, não é necessário se alistar.\033[0m")  

# Verificando se é a hora de se alistar
elif idade == 18:
    # Se for do sexo masculino, deve se alistar
    if sexo.lower() == "masculino":
        print("\033[32mVocê tem \033[33m18 anos.\033[32m É hora de \033[31mse alistar!\033[0m")
    # Se for do sexo feminino, não precisa se alistar
    else:
        print("\033[32mVocê tem \033[33m18 anos.\033[32m No entanto, como você é do sexo feminino, não é necessário se alistar.\033[0m")

# Verificando se já passou do tempo de alistamento
else:
    # Se for do sexo masculino, já deve ter se alistado
    if sexo.lower() == "masculino":
        print("\033[33mVocê já passou do tempo de alistamento.\n"
              "Já passaram\033[32m", idade - 18, "anos.\033[0m"
              f"Você já se alistou em {hoje.year - (idade - 18)}")
    # Se for do sexo feminino, não precisa se alistar
    else:
        print("\033[33mVocê já tem mais de 18 anos.\n"
        "No entanto, como você é do sexo feminino, não há necessidade de se alistar.\033[0m")

# Exibe uma mensagem informando a idade da pessoa  
print(f"Quem nasceu em {entrada_ano_nascimento} já tem {idade}anos")
