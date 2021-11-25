from tarjeta.tarjeta import Tarjeta
from tarjeta.entradas import lee_numero

class Tarjeta_de_Servicios(Tarjeta) :
    def capturar_tarjeta(self):
        """
        Captura los datos de una tarjeta
        """
        print("#"*50 +" Ingresar datos "+ "#"*50)

        self.asignar_nombre(input("Por favor digite el nombre de la tarjeta: "))        
        self.asignar_deuda_actual(float(lee_numero("Por favor digíte la deuda actual del crédito: ")))
        #self.asignar_pago(self.valida_pago(self.obtener_deuda_actual()))
        self.asignar_cargo(float(lee_numero("Por favor digíte el monto de los nuevos cargos: ")))
        
        print("#"*40 +" Fin de ingreso de datos "+ "#"*40)
        print()
    
    def valida_pago(self,deuda) :
        """
        Obtiene una entrada en donde valida que no sea mayor a la deuda
        recibe como parámetro el valor de la deuda
        """
        while True :
            pago = float(lee_numero("Por favor digíte el pago a realizar (solo se admite pago igual a la deuda): "))
            if  pago == deuda :  
                return pago
            else :    
                print("el valor pagado: {:.2f} no puede ser  diferente que la deuda: {:.2f}".format(pago,deuda))
    
    def capturar_pago(self):
        """ Captura el pago de la deuda """
        deuda = self.obtener_deuda_actual()
        self.asignar_pago( self.valida_pago(deuda) )

    def generar_reporte(self) :
        """
        Genera el reporte de una tarjeta
        """
        #Resumen
        print("-"*100)
        print("-"*100)

        print("#"*45 +" Resumen "+ "#"*45)
        print("Tarjeta: {:>38}".format(self.obtener_nombre()))        
        print("-"*100)
        print("Deuda actual: {:>36.2f}".format(self.obtener_deuda_actual()))
        print("Pago: {:>44.2f}".format(self.obtener_pago()))
        print("-"*100)
        print("Deuda recalculada: {:>31.2f}".format(self.obtener_deuda_recalculada()))
        print("Nuevos cargos: {:>35.2f}".format(self.obtener_cargo()))
        print("-"*100)
        print("Nueva deuda: {:>37.2f}".format(self.obtener_nueva_deuda()))
        print("#"*45 +" Fin de resumen "+ "#"*45)
        print()
