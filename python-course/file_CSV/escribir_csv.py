
import csv

columnas = ["nombre", "apellido","edad"]

dato = ["Paco","Botero",26]

datos_lista = [
    ["Paco","Botero",26],
    ["Javier","Quinonez",24],
    ["Emilio","tafur",25]
    ]
datos_dict = [
    {"nombre":"Paco","apellido":"Botero","edad":26},
    {"nombre":"javer","apellido":"Quinonez","edad":24},
    {"nombre":"Emilio","apellido":"Tafur","edad":25}
]


with  open("datos.csv","w",newline="") as archivo:
    writer = csv.DictWriter(archivo,fieldnames=columnas)
    writer.writeheader()
    writer.writerows(datos_dict)