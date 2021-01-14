import requests
import json
import datetime
import itertools

"""
Request has the following format:
GET /{lang}/datos/{category}/{widget}?[query-parameters]

Categories are:
- balance
- demanda
- generacion
- intercambios
- transporte
- mercados
"""

# URL ES
url = "https://apidatos.ree.es/es/datos/"
# caetgory_widget = "mercados/precios-mercados-tiempo-real" # time_trunc: hour
caetgory_widget = "mercados/componentes-precio-energia-cierre-desglose"
# caetgory_widget = "mercados/componentes-precio"

url = url + caetgory_widget

parameters = {
    "start_date": "2021-01-01T00:00",
    "end_date"  : "2021-01-02T00:00",
    "time_trunc": "month"
}

response = requests.get(url, params=parameters)

print("Response Status:\n", response.status_code)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print("Data:")
jprint(response.json())
