from tarjeta_de_servicios.tarjeta_de_servicios import Tarjeta_de_Servicios
from tarjeta.varios import borrar_terminal

def main():
    """ Programa principal """
    borrar_terminal()

    tarjeta = Tarjeta_de_Servicios()
    
    tarjeta.capturar_tarjeta()
    tarjeta.generar_reporte()

    tarjeta.capturar_pago()
    
    tarjeta.generar_reporte()

if __name__ == '__main__' :
    main()