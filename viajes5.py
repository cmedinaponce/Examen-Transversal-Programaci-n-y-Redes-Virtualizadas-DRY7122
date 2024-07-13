from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from datetime import datetime

def calcular_distancia_y_duracion(ciudad_origen, ciudad_destino, medio_transporte):
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

    # Definir velocidad promedio según el medio de transporte elegido
    if medio_transporte == "auto":
        velocidad_promedio_kmh = 100  # km/h
    elif medio_transporte == "avion":
        velocidad_promedio_kmh = 800  # km/h (suponiendo vuelo comercial)
    elif medio_transporte == "tren":
        velocidad_promedio_kmh = 120  # km/h (suponiendo tren de alta velocidad)
    else:
        return None, "Medio de transporte no válido."

    # Calcular la distancia geodésica entre las dos ciudades en kilómetros y millas
    distancia_km = geodesic(coord_origen, coord_destino).kilometers
    distancia_millas = geodesic(coord_origen, coord_destino).miles

    # Calcular la duración estimada del viaje
    duracion_horas = distancia_km / velocidad_promedio_kmh
    duracion_minutos = duracion_horas * 60

    return distancia_km, distancia_millas, duracion_horas, duracion_minutos

def generar_narrativa_viaje(ciudad_origen, ciudad_destino, distancia_km, distancia_millas, duracion_horas, duracion_minutos, medio_transporte):
    # Construir la narrativa del viaje
    narrativa = f"Viaje desde {ciudad_origen} hasta {ciudad_destino} en {medio_transporte}:\n"
    narrativa += f"- Distancia: {distancia_km:.2f} kilómetros / {distancia_millas:.2f} millas.\n"
    narrativa += f"- Duración estimada del viaje: {int(duracion_horas)} horas y {int(duracion_minutos)} minutos.\n"
    narrativa += "¡Buen viaje!"

    return narrativa

# Solicitar al usuario las ciudades de origen y destino
ciudad_origen = input("Ingrese la Ciudad de Origen (en Chile): ")
ciudad_destino = input("Ingrese la Ciudad de Destino (en Argentina): ")

# Solicitar al usuario el tipo de medio de transporte
print("Seleccione el medio de transporte:")
print("1. Auto")
print("2. Avión")
print("3. Tren")
opcion = input("Ingrese el número correspondiente al medio de transporte: ")

# Establecer la velocidad promedio según la opción seleccionada
if opcion == "1":
    medio_transporte = "auto"
elif opcion == "2":
    medio_transporte = "avion"
elif opcion == "3":
    medio_transporte = "tren"
else:
    print("Opción no válida.")
    exit()

# Calcular la distancia y duración entre las ciudades ingresadas
distancia_km, distancia_millas, duracion_horas, duracion_minutos = calcular_distancia_y_duracion(ciudad_origen, ciudad_destino, medio_transporte)

if distancia_km is None:
    print(distancia_millas)  # Manejar el caso de error
else:
    # Generar y mostrar la narrativa del viaje
    narrativa = generar_narrativa_viaje(ciudad_origen, ciudad_destino, distancia_km, distancia_millas, duracion_horas, duracion_minutos, medio_transporte)
    print(narrativa)