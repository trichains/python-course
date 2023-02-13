from datetime import date

# Obtém a data atual
hoje = date.today()

# Imprime o cabeçalho da Confederação Nacional de Natação
print("\n" + "-=-"*11 + "\nCONFEDERAÇÃO NACIONAL DE NATAÇÃO\n" + "-=-"*11)


# Recebe o ano de nascimento do usuário como entrada
ano_nascimento = int(input("Ano de nascimento: "))

# Calcula a idade do usuário com base na data atual e o ano de nascimento
idade = hoje.year - ano_nascimento

# Determina a categoria do nadador com base na idade
if idade <= 9:
    categoria = "MIRIM"
elif idade <= 14:
    categoria = "INFANTIL"
elif idade <= 19:
    categoria = "JUNIOR"
elif idade <= 20:
    categoria = "SÊNIOR"
else:
    categoria = "MASTER"

# Imprime a categoria da idade do nadador
print(f"O atleta tem {idade} anos.\n"
      f"sua categoria é {categoria}")