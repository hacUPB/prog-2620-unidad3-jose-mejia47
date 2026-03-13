# Solicitud dos números al usuario e imprimir los valores pares que hay entre dichos números

n1 = int(input("Ingresar el primer número: "))
n2 = int(input("Ingresar el segundo número: "))

# n1 = 10 y n2 = 25
# n1 = 67 y n2 = 4

# identificar ewl menor y mayor entre los dos
if n1 > n2:
    mayor = n1
    menor = n2
else:
    mayor = n2
    menor = n1

while menor <= mayor:
    if menor % 2 == 0:
        print(menor)
    menor =+ 1