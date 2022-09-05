from package.operaciones import sumar, restar, multiplicar, dividir
from package.hora import ir_a_casa


def main():
    # Ejercicio 1
    a = 6
    b = 3
    print(sumar(a, b))
    print(restar(a, b))
    print(multiplicar(a, b))
    print(dividir(a, b))

    # Ejercicio 2
    ir_a_casa()


if __name__ == "__main__":
    main()
