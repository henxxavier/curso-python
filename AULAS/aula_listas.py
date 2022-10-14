secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break  # Ele conta as chances

    letra = input('Digite uma letra: ') #O usuario digita uma letra.

    if len(letra) > 1: #tratamento de erro em caso de digitacao de mais de uma letra.
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue # Verificacao se o usuario digitou mais de uma letra.

    digitadas.append(letra) #inserindo cada letra digitada na lista digitadas.

    if letra in secreto: #Verificando se a letra digitada contem na palavra secreta.
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.') #deu certo imprima na tela uma mensagem positiva.
    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')#deu errado imprima uma mensagem negativa.
        digitadas.pop()#em caso de nao digitas a letra correta ele apaga da lista digitadas.

    secreto_temporario = '' # criou uma lista vazia para a palavra secreta temporaria.
    for letra_secreta in secreto: # criando uma var para conferir se a letra sectreta contem na lista digitas. Se sim ela e adicionada a lista secreto temporario.
        
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else: # se nao e adicionado um *
            secreto_temporario += '*'

    if secreto_temporario == secreto: # verifica se deu a palavra e igual a palavra secreta.
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else: #em caso negativo ela esta sendo substituida por um *
        print(f'A palavra secreta está assim: {secreto_temporario}') 

    if letra not in secreto: # se a letra nao bater com a letra secreta ele perde uma chance.
        chances -= 1 #subtraindo cada chance e adicionando a variavel.

    print(f'Você ainda tem {chances} chances.') #mostrando quantas chances ele tem.
    print()
