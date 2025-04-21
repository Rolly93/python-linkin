import json

#funciona para leer archivos en formato 'JSON'
with open("persona.json","r") as archivo_json:
    #desifrar los archivos o almancenar los datos del archivo JSON
    datos_json = json.load(archivo_json)

print(type(datos_json))
print(datos_json["nombre"])