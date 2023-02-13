# Lendo as notas do aluno
nota1 = float(input("Primeira nota: ")) # Lê a primeira nota do usuário
nota2 = float(input("Segunda nota: ")) # Lê a segunda nota do usuário

# Calculando a média das notas
media = (nota1 + nota2) / 2 # Soma as duas notas e divide pelo número de notas

# Verificando o resultado do aluno
if media < 5.0:
    resultado = "REPROVADO!" # Se a média for menor que 5.0, o aluno está reprovado
elif media > 5.0 and media < 6.9:
    resultado = "EM RECUPERAÇÃO!" # Se a média estiver entre 5.0 e 6.9, o aluno está em recuperação
else:
    resultado = "APROVADO!" # Se nenhuma das condições acima for verdadeira, o aluno está aprovado

# Imprimindo o resultado
print(f"Sua nota é {media:.1f} e você está {resultado}.") # Imprime a média e o resultado final do aluno