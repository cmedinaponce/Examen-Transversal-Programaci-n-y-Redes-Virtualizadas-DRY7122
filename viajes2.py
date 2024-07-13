from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def distancia_entre_ciudades(ciudad_origen, ciudad_destino):
    # Geolocalización de las ciudades
    geolocalizador = Nominatim(user_agent="calculo-distancia")

    # Obtener coordenadas de la ciudad de origen
    ubicacion_origen = geolocalizador.geocode(ciudad_origen + ", Chile")
    if not ubicacion_origen:
        return f"No se encontró la ubicación de {ciudad_origen}."

    # Obtener coordenadas de la ciudad de destino
    ubicacion_destino = geolocalizador.geocode(ciudad_destino + ", Argentina")
    if not ubicacion_destino:
        return f"No se encontró la ubicación de {ciudad_destino}."

    # Obtener las coordenadas (latitud, longitud) de cada ciudad
    coord_origen = (ubicacion_origen.latitude, ubicacion_origen.longitude)
    coord_destino = (ubicacion_destino.latitude, ubicacion_destino.longitude)

    # Calcular la distancia geodésica entre las dos ciudades
    distancia = geodesic(coord_origen, coord_destino).kilometers

    return distancia

# Solicitar al usuario las ciudades de origen y destino
ciudad_origen = input("Ingrese la Ciudad de Origen (en Chile): ")
ciudad_destino = input("Ingrese la Ciudad de Destino (en Argentina): ")

# Calcular la distancia entre las ciudades ingresadas
distancia = distancia_entre_ciudades(ciudad_origen, ciudad_destino)

if isinstance(distancia, str):
    print(distancia)  # Manejar el caso de error
else:
    print(f"La distancia entre {ciudad_origen} y {ciudad_destino} es aproximadamente {distancia:.2f} kilómetros.")