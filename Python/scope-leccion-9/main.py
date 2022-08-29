# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

def ingrese_paises():
    paises = input('Ingrese países, separarlos por coma (,):\n>> ')
    lista_paises = paises.split(',')
    for i, elemento in enumerate(lista_paises):
        lista_paises[i] = elemento.strip().title()

    lista_paises = list(set(lista_paises))
    lista_paises = sorted(lista_paises)

    return ', '.join(lista_paises)

if __name__ == '__main__':

    # Ejercicio 1
    print (ingrese_paises())