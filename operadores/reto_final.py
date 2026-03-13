edad_usuario = 17
saldo_billetera = 70.0
tiene_suscripcion_premium = True

precio_juego = 60

if tiene_suscripcion_premium:
    precio_final = precio_juego * 0.90  # 10% de descuento
else:
    precio_final = precio_juego

edad_valida = edad_usuario >= 17
saldo_suficiente = saldo_billetera >= precio_final

compra_exitosa = edad_valida and saldo_suficiente

print("Precio final del juego:", precio_final)
print("¿Compra exitosa?", compra_exitosa)