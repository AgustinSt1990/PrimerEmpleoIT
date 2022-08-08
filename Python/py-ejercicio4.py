peso = float(input('Ingrese su peso en Kilogramos: '))
estatura = float(input('Ingrese su estatur en metros: '))
imc = round(peso / estatura**2, 2)

comentario = 'Tu índice de masa corporal es donde es {}'

print (comentario.format(imc))