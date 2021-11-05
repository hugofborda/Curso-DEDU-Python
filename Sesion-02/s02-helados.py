MENU = ((1,"Helado con oreo",19),
    (2,"Helado con m&m",25),
    (3,"Helado con fresas",22),
    (4,"Helado con m&brownie",28),
    )

def leer_numero(mensaje) :
    while True:
       entrada = input(mensaje)
       try:
           entrada = int(entrada)
           return entrada
       except ValueError:
           print("El dato ingresado no es numérico, por favor ingrese de nuevo la información.")

def imprimir_menu(menu) :
    """ Imprime la lista de toppings en la salida estándar """
    print("#"*40)
    for x in menu:
        print(f"{x[0]} {x[1]}")
    print("#"*40)

def imprimir_precio(precio) :
    """ Imprime el precio del helado"""  
    if precio == -1 :
        print("La opción de helado seleccionada no está disponible")
    else :   
        print(f"El precio es: ${precio}")

def main() :
    """ Función principal del programa"""
    imprimir_menu(MENU)
    opcion :int = leer_numero("Seleccione la opción: ")

    if opcion > 0 and opcion <= len(MENU) :
        precio = MENU[opcion-1][2]
    else :
        precio = -1

    imprimir_precio(precio)

main()