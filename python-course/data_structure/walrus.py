def calcular_cuadrado(numero):
    return numero **2

lista_num = list(range(1,11))


lista_pares= []
for num in lista_num:
    #cuadrado = calcular_cuadrado(num)
        #operador walrus
    if (cuadrado := calcular_cuadrado(num)) %2 ==0:
        lista_pares.append(cuadrado)
#        print(f"el cuadrado de {num} es {cuadrado}, es un numero par")
#    else:
#        print(f"el cuadrado de {num} es {cuadrado}, es un numero impar")
print(lista_pares)


# variable             valiable           ciclo  condicion(   comprehension + walrus)
pares_comprehension = [cuadrado for num in lista_num if (cuadrado:=calcular_cuadrado(num)) %2==0]

print(pares_comprehension)