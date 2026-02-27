promedio = 8.5
nivel_socioeconomico = 1

condicion1 = promedio >= 9.0
condicion2 = nivel_socioeconomico == 1 and promedio > 8.0

beca = condicion1 or condicion2

print("El estudiante recibe beca?", beca)