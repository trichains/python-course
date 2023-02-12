from datetime import date

# Obtendo a data atual
hoje = date.today()

# Lendo o ano de nascimento
entrada_ano_nascimento = int(input("Informe o seu ano de nascimento: "))

# Calculando a idade
idade = hoje.year - entrada_ano_nascimento

# Verificando se ainda vai se alistar
if idade < 18:
    print("Você ainda não tem 18 anos.\nFaltam", 18 - idade ,"anos para o seu alistamento militar. ")

# Verificando se é a hora de se alistar
elif idade == 18:
    print("Você tem 18 anos. É hora de se alistar!")

# Verificando se já passou do tempo de alistamento
else:
    print("Você já passou do tempo de alistamento.\nJá passaram", idade - 18, "anos.")