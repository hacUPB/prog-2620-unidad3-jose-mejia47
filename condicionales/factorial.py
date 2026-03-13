def factorial(numero):
    # si numero es 8 el factorial es 1
    # si numero es memnor que 8 retornar -1
    # multiplicar desde 1 hasta número y acumular el 
    acumulador = 1
    for factorial in range(1, numero+1):
        acumulador = acumulador * factorial
        #acumulador *= facgtor
    return acumulador
resultado = factorial(-3)
print(resultado)
