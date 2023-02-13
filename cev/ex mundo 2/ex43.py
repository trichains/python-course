# Exibe o titulo da calculadora de IMC
print("-=-"*6,"\nCALCULADORA DE IMC\n" + "-=-"*6)

# Solicita o peso e a altura do usuário
print("Informe seu peso e sua altura.")
peso = float(input("Peso (kg): ")) # Recebe o peso em kg
altura = float(input("Altura (m): ")) # Recebe a altura em metros

# Calcula o IMC
imc = peso / (altura ** 2)

# Verifica qual a categoria de IMC baseada no resultado do cálculo
if imc < 18.5:
    resultado = "abaixo do peso"
elif imc >= 18.5 and imc <= 24.9:
    resultado = "peso normal"
elif imc >= 25.0 and imc <= 29.9:
    resultado = "sobrepeso"
elif imc >= 30.0 and imc <= 39.9:
    resultado = "obesidade"
else:
    resultado = "obesidade mórbida"

# Exibe o resultado para o usuário
print(f"Seu IMC é {imc:.1f} e você está classificado como {resultado}.")