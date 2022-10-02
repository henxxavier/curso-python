user_name = input('Digite seu nome de usuario: ')

if len(user_name) <= 4:
    print('Seu nome de usuario e pequeno demais')

elif len(user_name) <= 6:
    print('Seu nome de usuario e valido')

elif len(user_name) > 6: 
    print('Seu nome de usuario e grande demais')