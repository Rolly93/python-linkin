import csv
import os

ruta = "csv.vacio.csv"

ruta_absoluta_os = os.path.join(os.getcwd(),ruta)

print(ruta_absoluta_os)

#archivo_abierto =open(ruta,"w")
#writer = csv.writer(archivo_abierto,delimiter=",")
#archivo_abierto.close()