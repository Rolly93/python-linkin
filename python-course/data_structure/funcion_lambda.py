'''funciones lambda
lambda Variable : fucionamiento'''

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_pares =  list(filter(lambda numer : numer %2==0,lista_numeros))

nueva_lista = list(map(lambda numero :numero*10,lista_numeros))
print(nueva_lista,lista_pares)