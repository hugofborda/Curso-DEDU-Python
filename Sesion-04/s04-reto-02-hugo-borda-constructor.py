class Vehiculo() :
    velocidad : float
    numero_ruedas : int 
    medio : str 
    
    def __init__(self, velocidad, numero_ruedas, medio) -> None:
        """ Constructor de objeto velocidad"""
        self.velocidad : float = velocidad
        self.numero_ruedas : int = numero_ruedas
        self.medio : str = medio

    def __str__(self) -> str:
        """ Regresa la descripción de vehículo"""
        return f"Velocidad: {self.velocidad}, número de ruedas: {self.numero_ruedas}, medio: {self.medio}"        
  

def main() :
    """ Función principal"""
    print(Vehiculo(100.4,4,'Terrestre').__str__())
    input("Digíte cualquier tecla para continuar")
    print(Vehiculo(58.5,0,'Marítimo').__str__())
    input("Digíte cualquier tecla para continuar")
    print(Vehiculo(385,12,'Aéreo').__str__())
    input("Digíte cualquier tecla para continuar")

main()