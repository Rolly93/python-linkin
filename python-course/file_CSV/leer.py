import csv
import os

file = "python-course/file_CSV/datos.csv"
path = os.path.join(os.getcwd(),file)
with open(file,"r",encoding="UTF-8") as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        print(fila["nombre"])