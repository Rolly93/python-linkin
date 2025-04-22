import time

def medir_timepo_ejecucion(function):

    def wrapper(*arg,**kwargs):
        print("inicio de contabilizacion")
        inicio = time.time()
        function(*arg,**kwargs)
        fin = time.time()
        print(f"tiempo total de la ejecucion {fin-inicio}")
    return wrapper

def decorador_puntos(function):

    def wrapper(*arg,**kwargs):
        print(".....")
        function(*arg,**kwargs)
        print(".....")
    return wrapper

@decorador_puntos
@medir_timepo_ejecucion 
def recorrer_ciclo(rango):
    for i in range(rango):
        print(i)
        time.sleep(1)

recorrer_ciclo(5)