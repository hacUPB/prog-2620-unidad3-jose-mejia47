edad = int(input("Inegres su edad"))

if edad >= 0 and edad <= 125:
    if edad < 6:
        etapa = "Infancia"
    elif edad < 12:
        etapa = "Niñes"
    elif edad < 20:
        etapa = "Adolecencia"
    elif edad < 25:
        etapa = "Juventud"
    elif edad < 60:
        etapa = "Adultez"
    else:
        etapa = "Vejez"
    
    print(f"Asus {edad} años, Usted esta en la etapa de {etapa}")
else:
    print("El número ingresado no es una edad válida")
