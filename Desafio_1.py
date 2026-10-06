# Faça um código que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
# Exemplo de Resultado: O Seu salário atual é de R$1500,00 com o aumento de 15% seu novo salário será de R$1725,00
Salario = float(input('O Seu salário atual é de:'))
Aumento = Salario * 0.15
novo_salario = Salario + Aumento
print('Seu novo salario será:', novo_salario)
