#empaqueta solamente en par.
nombres=['paco','emilio','javier']
apellidos = ['botero','tafur','quinonez']

nombre_completo = list(zip(nombres,apellidos))
print(nombre_completo)
#desempaquetar
nombres_unzip,apellidos_unzip = zip(*nombre_completo)

print(nombres_unzip)
print(apellidos_unzip)

for nombre,apellido in zip(nombres,apellidos):
    print(nombre,apellido)