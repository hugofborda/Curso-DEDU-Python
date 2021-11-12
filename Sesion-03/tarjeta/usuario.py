from .tarjeta import crear_tarjeta, crear_tarjetas, generar_reportes, pago_recurrente, pagos_distintos
from .entradas import lee_numero

MENU = ((1,"Crear tarjetas"),
    (2,"Generar pago recurrente"),
    (3,"Generar pagos diferentes",22),
    )

def imprimir_menu(menu) :
    """ Imprime la lista de opciones de tarjetas """
    print("#"*40)
    for x in menu:
        print(f"{x[0]} {x[1]}")
    print("#"*40)

def seleccionar_opcion() :
    """ Función de selección de opción de menú """
    imprimir_menu(MENU)
    opcion :int = lee_numero("Seleccione la opción: ")

    if opcion == 1 :
        tarjetas_list :dict = crear_tarjetas()
        generar_reportes(tarjetas_list)
    if opcion == 2 :
        tarjeta_dict = crear_tarjeta()
        pago_recurrente(tarjeta_dict)
    if opcion == 3 :
        pagos_distintos()        
    else :
        "La opcion seleccionada no es valida"


def main() :
    """ Función principal"""    

if __name__ == '__main__' :
    main()
