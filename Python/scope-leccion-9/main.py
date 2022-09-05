from functools import reduce

# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.


def ingrese_paises():
    paises = input("Ingrese países, separarlos por coma (,):\n>> ")
    lista_paises = paises.split(",")
    for i, elemento in enumerate(lista_paises):
        lista_paises[i] = elemento.strip().title()

    lista_paises = list(set(lista_paises))
    lista_paises = sorted(lista_paises)

    return ", ".join(lista_paises)


# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter
# y realizará una suma de todos estos elementos obtenidos mediante reduce.


# si la funcion lambda impar
# entra en un map: se convierte en una mascara booleana (sirve para .sum())
# entra en un filter: aplica la mascara boolena
#
def suma_impares(lista):
    impar = lambda x: x % 2 != 0
    result = filter(impar, lista)

    sumar = lambda x, y: x + y
    result = reduce(sumar, list(result))
    return result


if __name__ == "__main__":

    # Ejercicio 1
    print(ingrese_paises())

    # Ejercicio 2
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(suma_impares(lista))
