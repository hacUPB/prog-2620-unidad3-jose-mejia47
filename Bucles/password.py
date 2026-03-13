# genere una constante de texto que será la contraseña. luego pída ál usuario que ingrese la contraseña. mientras la contraseña no sea la correcta, debe continuar a pedir la contraseña. si esta es correcta, se deja continuar al resto del programa

password = "contraseña"

texto = input("Ingrese la contraseña")

while password != texto:
    print("Contraseña invalida")
    texto = input("Ingrese la contraseña nuevamente")

print("Acceso permitido")
