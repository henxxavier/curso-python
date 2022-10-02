'''Definar variaveis com nome, peso, idade, altura e calcule ano da nascimento e imc de acordo com esses dados.'''

from datetime import date

nome = 'Henrique'
idade = 25
peso = 110
altura = 1.78
ano_atual = date.today().year
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, ')
print(f'Pesa {peso}Kg e o IMC de {nome} e de {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}')