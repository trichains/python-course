entrada_peso = float(input("Qual seu peso?: "))
entrada_altura = float(input("Qual sua altura?: "))
imc = entrada_peso / (entrada_altura ** 2)
if imc < 18:
    print(f"Seu peso foi {imc:.2f}\nVocê está abaixo do peso ideal!") 
elif imc > 25:
    print(f"Seu peso foi {imc:.2f}\nVocê está acima do peso ideal!")
else:
    print(f"Seu peso foi {imc:.2f}\nVocê está no seu peso ideal!")