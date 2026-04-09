```
INICIO

DEFINIR combustible_actual = 15000.0
DEFINIR reserva_legal = 2500.0
DEFINIR tramos_totales = 5
DEFINIR mision_completada = VERDADERO

FUNCIÓN calcular_consumo_tramo(distancia, viento):
    DEFINIR consumo_base = distancia * 3.5
    
    SI viento ES IGUAL A "contra" ENTONCES:
        RETORNAR consumo_base * 1.10
    SINO SI viento ES IGUAL A "favor" ENTONCES:
        RETORNAR consumo_base * 0.90
    SINO:
        RETORNAR consumo_base
    FIN SI
FIN FUNCIÓN

PARA tramo DESDE 1 HASTA tramos_totales HACER:
    IMPRIMIR " Iniciando Tramo", tramo, ""
    
    // Entradas de datos del usuario
    LEER distancia
    LEER viento
    
    // Invocación de función y proyección
    consumo = LLAMAR calcular_consumo_tramo(distancia, viento)
    combustible_proyectado = combustible_actual - consumo
    
    // Condicional de Seguridad (Evaluación de Reserva)
    SI combustible_proyectado <= reserva_legal ENTONCES:
        IMPRIMIR "¡ALERTA CRÍTICA! El consumo viola la reserva legal."
        IMPRIMIR "Protocolo de emergencia: Abortando ruta. Desviando al aeropuerto alterno."
        mision_completada = FALSO
        ROMPER BUCLE (Break)
    FIN SI
    
    // Actualización oficial de los tanques
    combustible_actual = combustible_proyectado
    IMPRIMIR "Combustible consumido:", consumo
    IMPRIMIR "Combustible restante a bordo:", combustible_actual
FIN PARA

SI mision_completada ES IGUAL A VERDADERO ENTONCES:
    IMPRIMIR " Vuelo completado con éxito. Aeronave en destino con reservas intactas."
FIN SI

FIN
```
