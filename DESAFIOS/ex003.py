'''Pergunte as horas e defina as saudacoes bom dia, boa tarde e boa noite.'''
hora = int(input('Que horas sao: '))
nome = 'Henrique'

if hora <= 11:
    print(f'Bom dia, {nome}!')

elif hora <= 17:
    print(f'Boa tarde, {nome}!')

elif hora <= 23:
    print(f'Boa noite, {nome}!')