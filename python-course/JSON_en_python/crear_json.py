import json

persona ={
    "nombre":"Javier",
    "apellido": "Quinonez",
    "edad":24
}

#para adentar u organizar el archivo JSON
#objeto_json = json.dumps(persona,indent=2)


with open("persona.json","w") as archivo_json:
    #para pasar los datos al archivo JSON
#    archivo_json.write(objeto_json)

    #sin indentar, se almacena de forma lineal
    json.dump(persona,archivo_json)