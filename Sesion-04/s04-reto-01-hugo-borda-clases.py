class Vehiculo() :
    velocidad : float
    numero_ruedas : int 
    medio : str 

    def definicion(self) -> str:
        """ Regresa la descripción de vehículo"""
        return f"Velocidad: {self.velocidad}, número de ruedas: {self.numero_ruedas}, medio: {self.medio}"        
      

def main() :
    """ Función principal"""
    v1 = Vehiculo()
    v1.velocidad = 100.4
    v1.numero_ruedas = 4
    v1.medio ='Terrestre'
    print(v1.definicion())
    
    v1 = Vehiculo()
    v1.velocidad = 100.4
    v1.numero_ruedas = 4
    v1.medio ='Terrestre'
    print(v1.definicion())
    
    v2 = Vehiculo()
    v2.velocidad = 58.5
    v2.numero_ruedas = 0
    v2.medio ='Marítimo'
    print(v2.definicion())

    v3 = Vehiculo()
    v3.velocidad = 385
    v3.numero_ruedas = 12
    v3.medio ='Aéreo'
    print(v3.definicion())


main()