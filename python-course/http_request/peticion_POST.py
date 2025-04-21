import requests

#url
url="https://webhook.site/ad5c8fe5-3b72-4bfe-a4a6-cde68ff667cd"

#datos para el rquest
payload = {
    "plato":"pasta",
    "cantidad":2
}

# datos para revisar quien solicicto
query_params={
    "nombre":"Paco"
}
#envio al post          url de pagina , insertacion de los datos,       para consulta en base de datos
response = requests.post(url,   data=payload , params=query_params)


