# Ejercicio
# 
# Crear un archivo ".py" donde creéis un archivo ".txt", lo abráis y escribáis dentro del archivo. 
# 
# Para ello, tendréis que acceder dos veces al archivo creado.

import os
def existe_archivo(ruta):
    """"Existe Archivo?
    
    Keyword arguments:
    ruta -- file_location
    Return: bool
    """
    return os.path.isfile(ruta)

def crear_txt(fichero):

    """Crear archivo nuevo
    
    Keyword arguments:
    nombre -- nombre del nuevo fichero ".txt"
    Return: crea un archivo en caso que no exista
    """
    
    if fichero.endswith('.txt') and not existe_archivo(fichero):
        f = open(fichero, 'x')

    elif not fichero.endswith('.txt') and not existe_archivo(fichero+'.txt'):
        f = open(fichero + '.txt', 'x')

    else:
        return False

    return f.close()


def escribe_txt(fichero, datos):

    # Acondicionamiento de datos
    contenido = []
    if isinstance(datos, type(list())):
        for linea in datos:
            if not linea.endswith('\n'):
                linea += '\n'
            contenido.append(linea)

    elif isinstance(datos, type(str())):
        if not datos.endswith('\n'):
            datos += '\n'
        contenido.append(datos)
    
    else:
        return print ('Solo funciono con listas y cadenas')
    
    # Manipulacion del fichero
    if isinstance(crear_txt(fichero), type(bool())):
        print ('Escribir un fichero existente')
        if not fichero.endswith('.txt'):
            fichero += '.txt'

        f = open(fichero, 'a')
        f.writelines(contenido)
        f.close()

    
    else:
        print ('Escribir un fichero nuevo')
        if not fichero.endswith('.txt'):
            fichero += '.txt'

        f = open(fichero, 'w')
        f.writelines(contenido)
        f.close()

def main():
    fichero = 'HelloWorld2'
    dato = '123'
    datos = ['123', 'abc', 'yo', 'tu', 'el']
    
    escribe_txt(fichero, datos)


if __name__ == '__main__':

    main()
