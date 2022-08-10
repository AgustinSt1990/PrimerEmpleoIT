# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self):
        if self.nota >= 6:
            return 'El alumno {}, obtuvo la nota {}, y está Aprobado'.format(self.nombre, self.nota)
        else:
            return 'El alumno {}, obtuvo la nota {}, y está Desaprobado'.format(self.nombre, self.nota)

if __name__ == '__main__':

    a = Alumno('Agustin', 10)

    print (a)