contador = 10
acumulador = 0
cpf = input('Digite o seu CPF: ')

while contador > 1:
    
    for valor in cpf[0:9]:
        multiplicacar_cpf = int(valor) * contador
        # print(f'{int(valor)} * {contador} = {multiplicacar_cpf}')
        acumulador += multiplicacar_cpf
        contador -= 1

        digito_1 = 11 - (acumulador % 11)
        if digito_1 > 9:
            digito_1 = 0           

contador = 11
while contador > 1:
    
    for valor in cpf[0:9]:
        multiplicacar_cpf = int(valor) * contador
        # print(f'{int(valor)} * {contador} = {multiplicacar_cpf}')
        acumulador += multiplicacar_cpf
        contador -= 1

        digito_2 = 11 - (acumulador % 11)
        if digito_2 > 9:
           digito_2 = 0

digito_1 = str(digito_1)
digito_2 = str(digito_2)

novo_cpf = cpf[0:9] + digito_1 + digito_2

if novo_cpf == cpf:
    print('CPF VALIDO!')
else:
    print('CPF INVALIDO!')