from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def calcular_distancia_y_duracion(ciudad_origen, ciudad_destino, medio_transporte):
    # Geolocalización de las ciudades
    geolocalizador = Nominatim(user_agent="calculo-distancia")

    # Obtener coordenadas de la ciudad de origen
    ubicacion_origen = geolocalizador.geocode(ciudad_origen + ", Chile")
    if not ubicacion_origen:
        return None, None, "No se encontró la ubicación de la ciudad de origen."

    # Obtener coordenadas de la ciudad de destino
    ubicacion_destino = geolocalizador.geocode(ciudad_destino + ", Argentina")
    if not ubicacion_destino:
        return None, None, "No se encontró la ubicación de la ciudad de destino."

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
        return None, None, "Medio de transporte no válido."

    # Calcular la distancia geodésica entre las dos ciudades en kilómetros y millas
    distancia_km = geodesic(coord_origen, coord_destino).kilometers
    distancia_millas = geodesic(coord_origen, coord_destino).miles

    # Calcular la duración estimada del viaje
    duracion_horas = distancia_km / velocidad_promedio_kmh
    duracion_minutos = duracion_horas * 60

    return distancia_km, distancia_millas, duracion_horas, duracion_minutos, None

def generar_narrativa_viaje(ciudad_origen, ciudad_destino, distancia_km, distancia_millas, duracion_horas, duracion_minutos, medio_transporte):
    # Construir la narrativa del viaje
    narrativa = f"Viaje desde {ciudad_origen} hasta {ciudad_destino} en {medio_transporte}:\n"
    narrativa += f"- Distancia: {distancia_km:.2f} kilómetros / {distancia_millas:.2f} millas.\n"
    narrativa += f"- Duración estimada del viaje: {int(duracion_horas)} horas y {int(duracion_minutos)} minutos.\n"
    narrativa += "¡Buen viaje!"

    return narrativa

def solicitar_ciudad(mensaje):
    while True:
        ciudad = input(mensaje)
        if ciudad.lower() == 's':
            return None
        if ciudad.strip():
            return ciudad.strip()

def solicitar_medio_transporte():
    while True:
        print("Seleccione el medio de transporte:")
        print("1. Auto")
        print("2. Avión")
        print("3. Tren")
        opcion = input("Ingrese el número correspondiente al medio de transporte (o 's' para salir): ").strip().lower()

        if opcion == 's':
            return None
        elif opcion == "1":
            return "auto"
        elif opcion == "2":
            return "avion"
        elif opcion == "3":
            return "tren"
        else:
            print("Opción no válida. Por favor, ingrese nuevamente.")

# Ciclo principal para realizar cálculos múltiples
while True:
    # Solicitar al usuario las ciudades de origen y destino
    ciudad_origen = solicitar_ciudad("Ingrese la Ciudad de Origen (en Chile) (o 's' para salir): ")
    if not ciudad_origen:
        break
    
    ciudad_destino = solicitar_ciudad("Ingrese la Ciudad de Destino (en Argentina) (o 's' para salir): ")
    if not ciudad_destino:
        break

    # Solicitar al usuario el tipo de medio de transporte
    medio_transporte = solicitar_medio_transporte()
    if not medio_transporte:
        break

    # Calcular la distancia y duración entre las ciudades ingresadas
    distancia_km, distancia_millas, duracion_horas, duracion_minutos, error = calcular_distancia_y_duracion(ciudad_origen, ciudad_destino, medio_transporte)

    if error:
        print(error)
    else:
        # Generar y mostrar la narrativa del viaje
        narrativa = generar_narrativa_viaje(ciudad_origen, ciudad_destino, distancia_km, distancia_millas, duracion_horas, duracion_minutos, medio_transporte)
        print(narrativa)

print("¡Gracias por usar el programa!")
