from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from datetime import datetime

def calcular_distancia_y_duracion(ciudad_origen, ciudad_destino):
    # Geolocalización de las ciudades
    geolocalizador = Nominatim(user_agent="calculo-distancia")

    # Obtener coordenadas de la ciudad de origen
    ubicacion_origen = geolocalizador.geocode(ciudad_origen + ", Chile")
    if not ubicacion_origen:
        return None, "No se encontró la ubicación de la ciudad de origen."

    # Obtener coordenadas de la ciudad de destino
    ubicacion_destino = geolocalizador.geocode(ciudad_destino + ", Argentina")
    if not ubicacion_destino:
        return None, "No se encontró la ubicación de la ciudad de destino."

    # Obtener las coordenadas (latitud, longitud) de cada ciudad
    coord_origen = (ubicacion_origen.latitude, ubicacion_origen.longitude)
    coord_destino = (ubicacion_destino.latitude, ubicacion_destino.longitude)

    # Calcular la distancia geodésica entre las dos ciudades en kilómetros
    distancia_km = geodesic(coord_origen, coord_destino).kilometers
    distancia_millas = geodesic(coord_origen, coord_destino).miles

    # Calcular la duración estimada del viaje (suponiendo una velocidad promedio de 100 km/h)
    velocidad_promedio_kmh = 100
    duracion_horas = distancia_km / velocidad_promedio_kmh
    duracion_minutos = duracion_horas * 60

    return distancia_km, distancia_millas, duracion_horas, duracion_minutos

# Solicitar al usuario las ciudades de origen y destino
ciudad_origen = input("Ingrese la Ciudad de Origen (en Chile): ")
ciudad_destino = input("Ingrese la Ciudad de Destino (en Argentina): ")

# Calcular la distancia y duración entre las ciudades ingresadas
distancia_km, distancia_millas, duracion_horas, duracion_minutos = calcular_distancia_y_duracion(ciudad_origen, ciudad_destino)

if distancia_km is None:
    print(distancia_millas)  # Manejar el caso de error
else:
    print(f"Distancia entre {ciudad_origen} y {ciudad_destino}:")
    print(f"- En kilómetros: {distancia_km:.2f} km")
    print(f"- En millas: {distancia_millas:.2f} mi")
    print(f"Duración estimada del viaje:")
    print(f"- En horas: {duracion_horas:.1f} horas")
    print(f"- En minutos: {duracion_minutos:.0f} minutos")