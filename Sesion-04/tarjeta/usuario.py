from .tarjeta import Tarjeta

class Usuario():
    """ Clase que define un usuario de tarjetas de crédito """
    def __init__(self, nombre) -> None:
       self.__nombre = nombre
       self.__tarjetas = []
    
    def __agregar_tarjeta(self,tarjeta) :
        """ Agrega una nueva tarjeta """
        self.__tarjetas.append(tarjeta)
    
    def __eliminar_tarjeta(self, tarjeta_eliminar) :
        """ Eliminar una tarjeta """
        tarjeta_eliminar :str = input("Digite el nombre de la tarjeta a eliminar: ")
        for tarjeta in self.__tarjetas :
            if tarjeta_eliminar == tarjeta.obtener_nombre() :
                self.__tarjetas.remove(tarjeta)
                return True
            else :
                return False
    
    def imprimir_tarjetas(self) :
        for tarjeta in self.__tarjetas :
            tarjeta.generar_reporte()

    def eliminar_tarjeta(self) :
        """ Eliminar una tarjeta solicitada por entrada estándar"""
        tarjeta_eliminar :str = input("Digite el nombre de la tarjeta a eliminar: ")
        if self.__eliminar_tarjeta(tarjeta_eliminar):
            print(f"La tarjeta :{tarjeta_eliminar} ha sido eliminada.")
        else :
            print(f" No fue posible eliminar la tarjeta: {tarjeta_eliminar}, no se encuentra en el listado de tarjetas.")

    def eliminar_ultima_tarjeta(self) :
        tarjeta_eliminar = self.__tarjetas[-1].obtener_nombre()
        self.__tarjetas.pop()
        print("#"*50 +" Tarjeta eliminada "+ "#"*50)
        print(f"La tarjeta: {tarjeta_eliminar}, ha sido eliminada.")
        print("#"*50 +" Tarjeta eliminada "+ "#"*50)

    def agregar_tarjeta(self) :
        """ Agrega una nueva tarjeta """
        tarjeta = Tarjeta()
        tarjeta.capturar_tarjeta()
        self.__agregar_tarjeta(tarjeta)
            
