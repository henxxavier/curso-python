from datetime import date

nome = 'Henrique Xavier'
idade = 25
peso = 110
altura = 1.78
ano_atual = date.today().year
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos ')
print(f'pesa {peso}Kg e o IMC de {nome} e de {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}')