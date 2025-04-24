'''Creacion de Metodos 'Closure' 

para ser una funcion (closure) tiene que cumplir con la siguientes condicones

tener debe de ser una funcion anidada donde la funcion principal tiene que devolver la funcion que interna.

ejemplo:
'''

def agregar_persona_directorio():
    directorio = {}
    def agregar(nombre,edad,ciudad):
        directorio[nombre] = {
            "edad":edad,
            "ciudad":ciudad
        }
        return directorio
    return agregar
almacenar = agregar_persona_directorio()
directorio = almacenar("Paco",27,"Cali")
directorio = almacenar("Javier",25,"Madrid")

print(directorio)
