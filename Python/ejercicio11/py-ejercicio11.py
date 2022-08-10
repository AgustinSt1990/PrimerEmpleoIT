# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

# Color
# Ruedas
# Puertas

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

# Velocidad
# Cilindrada

# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:
    color = 'blanco'
    ruedas = 5
    puertas = 4

class Coche(Vehiculo):
    velocidad = 130
    cilindrada = 1500

if __name__ == '__main__':
    v = Coche()
    print (
    'color: ',v.color, '\n', \
    'ruedas: ',v.ruedas, '\n', \
    'puertas: ',v.puertas, '\n', \
    'velocidad: ',v.velocidad, '\n', \
    'cilindrada: ',v.cilindrada, '\n'
    )