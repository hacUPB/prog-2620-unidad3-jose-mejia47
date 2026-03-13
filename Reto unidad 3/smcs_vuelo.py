# --- DECLARACIÓN DE USO DE IA ---
# Parte de la estructura lógica de este código fueron asistidos por IA, ajustados para cumplir con las normativas del reto.

def calcular_consumo_tramo(distancia, viento):
    consumo_base = distancia * 3.5
    
    if viento == "contra":
        consumo_final = consumo_base * 1.10
    elif viento == "favor":
        consumo_final = consumo_base * 0.90
    else:
        consumo_final = consumo_base
        
    return consumo_final

print("INICIANDO SISTEMA SMCS")

combustible_actual = 15000.0
reserva_legal = 2500.0
tramos_totales = 5
mision_completada = True

for tramo in range(1, tramos_totales + 1):
    print(f"\n--- Iniciando Tramo {tramo} ---")
    
    distancia_str = input("Ingrese la distancia del tramo en km: ")
    distancia = float(distancia_str)
    viento = input("Ingrese la condición del viento (contra / favor / nulo): ").lower()
    consumo = calcular_consumo_tramo(distancia, viento)
    combustible_proyectado = combustible_actual - consumo
    
    if combustible_proyectado <= reserva_legal:
        print("\n ¡ALERTA CRÍTICA! ")
        print(f"El consumo proyectado dejará el tanque en {combustible_proyectado} kg.")
        print(f"Esto viola la reserva legal de {reserva_legal} kg.")
        print("Protocolo de emergencia activado: Abortando ruta. Desviando al aeropuerto alterno más cercano.")
        mision_completada = False
        break 

    combustible_actual = combustible_proyectado
    print(f"Combustible consumido en tramo: {consumo} kg")
    print(f"Combustible restante a bordo: {combustible_actual} kg")

if mision_completada == True:
    print("\n Vuelo completado con éxito. Aeronave en destino con reservas intactas.")