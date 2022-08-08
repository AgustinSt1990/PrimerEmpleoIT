def mayorEdad():
    while True:
        try:
            edad = int(input('Ingresa tu edad: '))
            resultado = ['Es mayor de edad' if edad >= 18 else 'Es menor de edad'][0]
            return print (resultado)
        except:
            print ('El valor ingresado no es correcto')


if __name__ == '__main__':
    mayorEdad()