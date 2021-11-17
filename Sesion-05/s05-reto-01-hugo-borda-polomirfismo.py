class Vehiculo() :
    """ Clase que define vahículos """
    def __init__(self, velocidad, medio) -> None:
        """ Constructor de objeto vehículo """
        self.__velocidad : float = velocidad        
        self.__medio : str = medio

    def asignar_medio(self, medio) :
        """ Asigna medio """
        self.__medio = medio

    def asignar_velocidad(self, velocidad) :
        " Asgina velocidad "
        self.__velocidad = velocidad    

    def __str__(self) -> str:
        """ Regresa la descripción de vehículo"""
        return f"Velocidad: {self.__velocidad}, medio: {self.__medio}"       
    
    def avanzar():
        """ Imprime mensaje """
        print("Vehículo avanza")
 

class Aereos(Vehiculo) :
    """ Clase que define los vehículos aéreos """
      
    def __init__(self, velocidad,helices) -> None:
        super().__init__(velocidad, "Aéreos")
        self.asignar_numero_helices(helices)

    def asignar_numero_helices(self, numero_helices) :
        """ Asigna número de elices """
        self.__numero_helices = numero_helices
    
    def __str__(self) -> str:
        """ Regresa la descripción de aéreos"""
        return super().__str__() + f", número de hélices: {self.__numero_helices}"

    def avanzar():
        """ Imprime mensaje """
        print("Vehículo avanza por el aire")        

class Terrestres(Vehiculo) :
    """ Clase que define los vehículos terrestres"""    

    def __init__(self, velocidad, numero_ruedas) -> None:
        """ Constructor de objeto vehículo terrestre """
        self.asignar_numero_ruedas(numero_ruedas)
        super().__init__(velocidad, "Terrestre")

    def asignar_numero_ruedas(self, numero_ruedas) :
        """ Asigna número de ruedas """
        self.__numero_ruedas = numero_ruedas
    
    def __str__(self) -> str:
        """ Regresa la descripción de vehículo"""
        return super().__str__() + f", número de ruedas: {self.__numero_ruedas}"
    
    def avanzar():
        """ Imprime mensaje """
        print("Vehículo avanza por la tierra")        



class Acuaticos(Vehiculo) :
    """ Clase que define los vehículos acuáticos"""    

    def __init__(self, velocidad, aspas) -> None:
        """ Constructor de objeto vehículo acuático """
        super().__init__(velocidad, "Acuáticos")
        self.asignar_aspas(aspas)

    def asignar_aspas(self, aspas) :
        """ Asigna número de aspas """
        self.__aspas = aspas
    
    def __str__(self) -> str:
        """ Regresa la descripción de acuáticos"""
        return super().__str__() + f", número de aspas: {self.__aspas}"
    
    def avanzar():
        """ Imprime mensaje """
        print("Vehículo avanza por el agua")        
  

def main() :
    """ Función principal"""
    v1 = Terrestres(100.4,4)
    v1.__numero_ruedas = 5
    print(v1)
    input("Digíte cualquier tecla para continuar")
    
    print(Aereos(385,4))
    input("Digíte cualquier tecla para continuar")

    print(Acuaticos(58.4,2))
    input("Digíte cualquier tecla para continuar")

main()