import requests

# Coordenadas de *
LATITUDE =
LONGITUDE =

url = "https://api.open-meteo.com/v1/forecast"

parametros = {
    "longitude": LONGITUDE,
    "latitude": LATITUDE,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "timezone": "auto"
}

response = requests.get(url, params= parametros)
data = response.json()

# Extraindo informações
clima_atual = data["current"]
temperatura = clima_atual["temperature_2m"]
umidade = clima_atual["relative_humidity_2m"]
vento = clima_atual["wind_speed_10m"]

print(f"--- ** ---")
print(f"Temperatura: {temperatura}°C")
print(f"Umidade: {umidade}%")
print(f"Velocidade do vento: {vento} km/h")
