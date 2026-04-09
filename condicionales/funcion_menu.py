def menu():
    # No se debe permitir seleccionar una opción que no está
    opcion = 0
    while opcion < 1 or opcion > 4:
     print("1, Asesor1, Asesor2, Asesor3, Coordinador")
    opcion = int(input("seleccione una opción: "))
    if opcion < 1 or opcion > 4:
        print("opción elegida no valida.../n")
    return opcion

operacion = menu
print(f"El ususario elegió la opcion {operacion}")

def menu():
 print("1, Asesor1, Asesor2, Asesor3, Coordinador")
 opcion = int(input("seleccione una opción: "))
 