# var = ['Henrique','Fabiola','Mateus']
# letra = input('Digite uma letra: ').upper()

# for valor in var:
#     if valor.startswith(letra):
#         print(f'A palavra {valor} comeca com a letra {letra}')
#         break
# else:
#     print(f'Nao existe nenhuma palavra que comeca com a letra {letra}'


string = 'O Brasil e o pais do futebol, o brasil e penta'

lista_1 = string.split(' ')

palavra = ''
contagem = 0

for valor in lista_1:
    qtd_vezes = lista_1.count(valor)
    
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra qeu apareceu mais vezes e {palavra} ({contagem}x)')