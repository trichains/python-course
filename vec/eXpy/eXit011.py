a=float(input('Qual a Altura da Parede?: '))
l=float(input('Qual a Largura da Parede?: '))
print(f'Sua parede tem a dimensão de\n{a} de altura e {l} de largura.\nA área tem {a*l:.2f}m².\nPara pintar essa parede, você precisará de {(a*l)/2:.1f}L de tinta')