'''
con condicion
lista = [expresion(elemento) for elemento in objeto_iterable if condicion]

sin condicon
lista = [expresoin(elemento) for elemento in objeto_iterable]
'''

def calcular_cuadrado(numero):
    return numero**2

def es_par(numero):
    return numero %2==0

lista_num=[1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = [calcular_cuadrado(num) for num in lista_num]
print(f"list comprehension:\t",lista_cuadrados)


lista_cuadrados_pares = [ calcular_cuadrado(num) for num in lista_num if es_par(num)]

print("list comprehension con condicion \t",lista_cuadrados_pares)

# se define una variable , [ se declara al funcion a utilizar , se coloca la condicon 'if' des ser necesario se coloca una segunda condicon 'else' , se declara la cicle a utilizar]
lista_resultados = [ calcular_cuadrado(num) if es_par(num) else 0 for num in lista_num]

print(f"list comprehension con 2 condiciones \t",lista_resultados)