# Se o salário do funcionário for maior que 1250.00R$ ele receberá um aumento de 10%
# Se o salário do funcionário for menor ou igual a 1250.00R$ ele receberá um aumento de 15%

sal=(float(input('Qual o salário do funcionário?: R$')))
if sal > 1250.00:
    aumento = (sal * 10 / 100) # multiplica o salário por 10 e divide por 100, bota o resultado dentro da variavel "aumento"
    novo = sal + aumento # soma a variavel "aumento" com o valor do salário.
    print(f'O salário do funcionário era de R${sal:.2f}.\n Com o aumento de 10% ("R${aumento:.2f}"), o salário passou a ser de R${novo:.2f}')
else:
    aumento = (15 / 100 * sal) # divide 15 por 100 e multiplica pelo valor do salário.
    novo = sal + aumento # agora é só somar o resultado com o salario.
    print(f'O salário do funcionário era de R${sal:.2f}.\nCom o aumento de 15% ("R${aumento:.2f}"), o salário passou a ser de R${novo:.2f}')