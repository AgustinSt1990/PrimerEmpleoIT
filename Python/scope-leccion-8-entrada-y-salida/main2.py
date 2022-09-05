# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.


class Vehiculo:
    def __init__(self, marca: str, modelo: str, fecha_fab: int, km_acum: int):

        self.marca = marca
        self.modelo = modelo
        self.fecha_fab = fecha_fab
        self.km_acum = km_acum

    def __str__(self):
        return (
            f"Vehículo:\n\t- Marca: {self.marca} \n\t- Modelo: {self.modelo}\n"
            f"\t- Fecha de Fabricación: {self.fecha_fab} \n\t- Kilometraje Acumulado: {self.km_acum}\n"
        )


def save_state(element):
    import pickle

    filename = input("Nombre del fichero: ")
    if not filename.endswith(".bin"):
        filename += ".bin"

    f = open(filename, "wb")
    pickle.dump(element, f)
    f.close()


def load_state(filename):
    import pickle

    if not filename.endswith(".bin"):
        filename += ".bin"

    f = open(filename, "rb")
    element = pickle.load(f)
    f.close()
    return element


def main():
    c1 = Vehiculo("WV", "Golf TDi", 2011, 110000)
    save_state(c1)

    # c1_load = load_state('VW.bin')
    # print (c1_load)


if __name__ == "__main__":
    main()
