from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def distancia_entre_ciudades(ciudad_chile, ciudad_argentina):
    # Geolocalización de las ciudades
    geolocalizador = Nominatim(user_agent="calculo-distancia")

    # Obtener coordenadas de la ciudad en Chile
    ubicacion_chile = geolocalizador.geocode(ciudad_chile + ", Chile")
    if not ubicacion_chile:
        return "No se encontró la ubicación de la ciudad en Chile."

    # Obtener coordenadas de la ciudad en Argentina
    ubicacion_argentina = geolocalizador.geocode(ciudad_argentina + ", Argentina")
    if not ubicacion_argentina:
        return "No se encontró la ubicación de la ciudad en Argentina."

    # Obtener las coordenadas (latitud, longitud) de cada ciudad
    coord_chile = (ubicacion_chile.latitude, ubicacion_chile.longitude)
    coord_argentina = (ubicacion_argentina.latitude, ubicacion_argentina.longitude)

    # Calcular la distancia geodésica entre las dos ciudades
    distancia = geodesic(coord_chile, coord_argentina).kilometers

    return distancia

# Ejemplo de uso
ciudad_chile = "Santiago"
ciudad_argentina = "Buenos Aires"
distancia = distancia_entre_ciudades(ciudad_chile, ciudad_argentina)

if isinstance(distancia, str):
    print(distancia)  # Manejar el caso de error
else:
    print(f"La distancia entre {ciudad_chile} y {ciudad_argentina} es aproximadamente {distancia:.2f} kilómetros.")