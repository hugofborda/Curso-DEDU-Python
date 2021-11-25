def lee_numero(mensaje) :
    """
    Obtiene una entrada estándar la cual valida que sea un número
    recibe un parámetro de entrada que indica el mensaje a mostrar en la entrada.
    """
    while True:
       entrada = input(mensaje)
       try:
           entrada = float(entrada)
           return entrada
       except ValueError:
           print("El dato ingresado no es numérico, por favor ingrese de nuevo la información.")

def lee_S_N(mensaje) :
    """
    Obtiene una entrada estándar la cual valida que sea s o n
    recibe un parámetro de entrada que indica el mensaje a mostrar en la entrada.
    """
    while True:
        entrada_str = input(mensaje)
        if entrada_str.lower() == 's' or entrada_str.lower() == 'n' :
           return entrada_str
        else :
            print("La opción digitada no es S o N.")

def obtener_pagos():
    """
    Obtiene la entrada de pagos diferentes
    """
    lista_pagos = []
    while True :
        pago : float = lee_numero("Escriba la cantidad del siguiente pago (Escriba 0 para terminar: ")
        if pago == 0 :
            return lista_pagos
        else :
            lista_pagos.append(pago)

def main() :
    """ Función principal"""    

if __name__ == '__main__' :
    main()


