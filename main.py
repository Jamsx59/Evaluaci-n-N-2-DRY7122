import requests

def obtener_distancia_y_duracion(origen, destino, token):
    url = f"http://www.mapquestapi.com/directions/v2/route?key={token}&from={origen}&to={destino}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and data["info"]["statuscode"] == 0:
        distancia = round(data["route"]["distance"], 2)
        duracion_segundos = data["route"]["time"]
        duracion_horas = duracion_segundos // 3600
        duracion_minutos = (duracion_segundos % 3600) // 60
        duracion_segundos = duracion_segundos % 60
        narrativa = data["route"]["formattedTime"]
        return distancia, duracion_horas, duracion_minutos, duracion_segundos, narrativa
    
    return None

def main():
    token = "1IFb2oDYsg21vYZZqyQyJDBTtv3W06hO"

    while True:
        opcion = input("Ingrese 'q' para salir o cualquier otra tecla para continuar: ")
        
        if opcion.lower() == "q":
            break

        origen = input("Ingrese la ciudad de origen: ")
        destino = input("Ingrese la ciudad de destino: ")

        resultado = obtener_distancia_y_duracion(origen, destino, token)

        if resultado is not None:
            distancia, duracion_horas, duracion_minutos, duracion_segundos, narrativa = resultado
            print(f"La distancia entre {origen} y {destino} es de {distancia:.2f} kilómetros.")
            print(f"La duración del viaje es de {duracion_horas:.0f} horas, {duracion_minutos:.0f} minutos y {duracion_segundos:.0f} segundos.")
            print(f"Narrativa del viaje: {narrativa}")
        else:
            print("Error al obtener la información. Verifique las ciudades ingresadas o el token de MapQuest.")

if __name__ == "__main__":
    main()

