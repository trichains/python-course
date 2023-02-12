from datetime import date

# Obtém a data atual
hoje = date.today()

# Imprime o cabeçalho da Confederação Nacional de Natação
print("\n" + "-=-"*11 + "\nCONFEDERAÇÃO NACIONAL DE NATAÇÃO\n" + "-=-"*11)


# Recebe o ano de nascimento do usuário como entrada
entrada_ano_nascimento = int(input("Digite seu ano de nascimento: "))

# Calcula a idade do usuário com base na data atual e o ano de nascimento
categoria = hoje.year - entrada_ano_nascimento

# Determina a categoria do nadador com base na idade
if categoria <= 9:
    resultado = "MIRIM"
elif categoria <= 14:
    resultado = "INFANTIL"
elif categoria <= 19:
    resultado = "JUNIOR"
elif categoria <= 20:
    resultado = "SÊNIOR"
else:
    resultado = "MASTER"

# Imprime o resultado da categoria do nadador
print(f"Como você tem {categoria} anos de idade, sua categoria é {resultado}")
