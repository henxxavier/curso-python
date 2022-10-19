contador = 10
acumulador = 0
cpf = input('Digite o seu CPF: ')

while contador > 1:
    
    for valor in cpf[0:9]:
        multiplicacar_cpf = int(valor) * contador
        print(f'{int(valor)} * {contador} = {multiplicacar_cpf}')
        acumulador += multiplicacar_cpf
        contador -= 1

print(acumulador)

digito_1 = 11 - (acumulador % 11)
if digito_1 > 9:
    digito_1 = 0
    
print(digito_1)
