from tarjeta.usuario import Usuario
from tarjeta.tarjeta import Tarjeta
from tarjeta.varios import borrar_terminal
def main():
    """ Programa principal """
    borrar_terminal()

    usuario = Usuario("Juan")

    usuario.agregar_tarjeta()
    usuario.agregar_tarjeta()
    usuario.agregar_tarjeta()
    usuario.imprimir_tarjetas()
    
    usuario.eliminar_ultima_tarjeta()
    
    usuario.imprimir_tarjetas()

if __name__ == '__main__' :
    main()