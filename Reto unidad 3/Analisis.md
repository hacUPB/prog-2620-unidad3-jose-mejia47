## Valores Técnicos Investigados y Justificados de una Airbus A320:

### Consumo Base:
3.5 kg/km, (Es un promedio realista en altitud de crucero para un bimotor comercial de fuselaje estrecho)

### Efecto Viento en Contra: 
Aumento del 15%, El avión necesita generar más empuje (mayor flujo de combustible) para mantener su velocidad respecto al suelo y cumplir con el tiempo de ruta.

### Efecto Viento a Favor:
Reducción del 10%, El viento de cola empuja la aeronave, permitiendo a los motores operar con menor régimen de potencia mientras se mantiene la velocidad de crucero.

### Reserva Legal:
2,500 kg, Por normativa aeronáutica, esto cubre aproximadamente 45 minutos de vuelo en patrón de espera, más el combustible necesario para desviarse al aeropuerto alterno más cercano.

### Capacidad Inicial:
15,000 kg.


## Inputs
| Variable | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| distancia | Numérico (Float) | Los kilómetros a recorrer en el tramo actual. |
| viento | Texto (String) | Condición del viento: "contra", "favor", "cruzado", "nulo". |

## Outputs
| Variable | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| consumo_tramo | Numérico (Float) | Kilogramos de combustible quemados en el tramo. |
| combustible_actual | Numérico (Float) | Kilogramos restantes en los tanques tras el tramo. |
| alerta | Texto (String) | Mensaje de advertencia si se compromete la reserva. |

## Constantes y Variables de Control
| Elemento | Valor / Estado | Rol en el Bucle |
| :--- | :--- | :--- |
| consumo_base_jm | 3.5 | Constante para el cálculo base. |
| reserva_legal | 2500.0 | Constante que define el límite de seguridad. |
| combustible_actual | Inicia en 15000.0 | Variable que disminuye en cada iteración. |
| tramo_actual | 1 a 5 | Variable de control que hace que el bucle avance. |