class Vehiculo() :
    def __init__(self, velocidad, numero_ruedas, medio) -> None:
        """ Constructor de objeto velocidad"""
        self.__velocidad : float = velocidad
        self.__numero_ruedas : int = numero_ruedas
        self.__medio : str = medio

    def asignar_medio(self, medio) :
        self.__medio = medio

    def asignar_velocidad(self, velocidad) :
        self.__velocidad = velocidad    

    def asignar_numero_ruedas(self, numero_ruedas) :
        self.__numero_ruedas = numero_ruedas

    def __str__(self) -> str:
        """ Regresa la descripción de vehículo"""
        return f"Velocidad: {self.__velocidad}, número de ruedas: {self.__numero_ruedas}, medio: {self.__medio}"        
  

def main() :
    """ Función principal"""
    v1 = Vehiculo(100.4,4,'Terrestre')
    v1.__numero_ruedas = 5
    print(v1)
    input("Digíte cualquier tecla para continuar")
    print(Vehiculo(58.5,0,'Marítimo').__str__())
    input("Digíte cualquier tecla para continuar")
    print(Vehiculo(385,12,'Aéreo').__str__())
    input("Digíte cualquier tecla para continuar")

main()