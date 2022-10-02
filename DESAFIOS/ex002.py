import re
 
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)

num = int(input('Digite um numero inteiro: '))

if is_number(num):
    if is_int(num):
        resto = num % 2
        if resto == 0:
            print(f'O numero {num} e PAR')
        else:
            print(f'O numero {num} e IMPAR')

    elif is_float(num):
        print('Digite um numero inteiro.')
else:
    print('Erro, isso nao e um numero.')