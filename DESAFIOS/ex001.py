from datetime import date

nome = 'Henrique Xavier'
idade = 25
peso = 110
altura = 1.78
ano_atual = date.today().year
ano_nascimento = ano_atual - idade
imc = peso / (altura * altura)

print(f'{nome} tem {idade} anos e nasceu em {ano_nascimento}')
print(f'O IMC de {nome} e de {imc}')