#enumerate(iterable,start=0)
nombres = [ 'paco','emilio','javier','ana']

nombres_enumerados=enumerate(nombres,start=5)

for indice,elemento in enumerate(nombres):
    print(indice,elemento)