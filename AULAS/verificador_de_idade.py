name_global = []
age_global = []
weight_global = []
height_global = []


for c in range(1,3):
    print('='*15)
    name = input('Digite o seu nome: ')
    name_global.append(name)
    
    age = int(input('Digite a sua idade: '))
    age_global.append(age)
    
    weight = float(input('Digite o seu peso: '))
    weight_global.append(weight)
    
    height = float(input('Digite a sua altura: '))
    height_global.append(height)

for maior_idade in age_global:
    print(maior_idade)