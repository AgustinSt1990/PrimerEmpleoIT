# determinar si un año es Biciesto
# 1ro. Si un año es divisble por 100, son biciestos solo si son divisibles por 400
# 2do. Sino todos los años divisibles por 4, son biciestos


def biciesto():
    year = input("Escoge un año: ")

    if len(year) >= 5:
        print("El tope son 4 cifras")

    try:
        year = int(year)
    except:
        print("Dato no reconocido")
        return

    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False

    elif year % 4 == 0:
        return True

    else:
        return False


if __name__ == "__main__":

    a = biciesto()

    print(f"Biciesto = {a}")
