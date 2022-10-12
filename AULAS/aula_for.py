texto = 'python'
nova_string = ''

for letra in texto:
    if letra == 't' or letra == 'h'  or letra == 'o':
        nova_string += letra.upper()
    else: 
        nova_string += letra
        
print(nova_string) 