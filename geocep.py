from geopy.geocoders import Nominatim
import random2

def encontrar_lat_long_por_cep(cep):
    nome_aleatorio = random2.randint(0, 10000)
    nome_aleatorio_string = str(nome_aleatorio)
    geolocator = Nominatim(user_agent=f"{nome_aleatorio_string}")
    location = geolocator.geocode(cep)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

#cep = "26070-132"

#lista de ceps
cep_list = ["26070-132","05407-002"]
for cep in cep_list:

    latitude, longitude = encontrar_lat_long_por_cep(cep)
    if latitude and longitude:
        #Exportando os dados para um arquivo desejado
        with open("geocep.txt", "a") as file:
            
            file.write(f"A latitude e longitude do CEP {cep} são: ({latitude}), ({longitude})\n")
    else:
        print(f"Não foi possível encontrar a localização para o CEP {cep}")
print("Concluído!")