""""
lista = [ expresion(element) for elemento in objeto_iterable]
"""
def calcular_cuadrado(numero):
    return numero**2

lista_num = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = []

for num in lista_num:
    cuadrado = num **2
    lista_cuadrados.append(cuadrado)

print(f"ciclo for:\t {lista_cuadrados} ")

list_comprehension = [ num**2 for num in lista_num]
print(f"List comprehension\t{list_comprehension}")

list_comprehension = [ calcular_cuadrado(num) for num in lista_num]
print(f"List Con metodos\t{list_comprehension}")