from utilidades.entradas import lee_numero
import json


class Tarjeta() :
    """ Clase que define una tarjeta de crédito"""
    __nombre : str
    __interes_anual : float
    __deuda_actual : float
    __pago : float
    __cargo : float 

    def __init__(self, nombre=None, interes_anual=0, deuda_actual=0, pago=0, cargo=0) -> None:
        self.asignar_nombre(nombre)
        self.asignar_interes_anual(interes_anual)
        self.asignar_deuda_actual(deuda_actual)
        self.asignar_pago(pago)
        self.asignar_cargo(cargo) 

    @property
    def dict(self) :
        tarjeta_dict = {}
        tarjeta_dict["nombre"] = self.obtener_nombre()
        tarjeta_dict["interes_anual"] = self.obtener_interes_anual()
        tarjeta_dict["deuda_actual"] = self.obtener_deuda_actual()
        tarjeta_dict["pago"] = self.obtener_pago()
        tarjeta_dict["cargo"] = self.obtener_cargo()
        return tarjeta_dict

    def asignar_nombre(self, nombre) :
        """ Asigna nombre """
        self.__nombre = nombre

    def asignar_interes_anual(self, interes_anual) :
        """ Asigna interés anual """
        self.__interes_anual = interes_anual

    def asignar_deuda_actual(self, deuda_actual) :
        """ Asigna deuda actual """
        self.__deuda_actual = deuda_actual

    def asignar_pago(self, pago) :
        """ Asigna pago """
        self.__pago = pago                

    def asignar_cargo(self, cargo) :
        """ Asigna cargo """
        self.__cargo = cargo  

    def obtener_nombre(self) :
        """ Obtiene nombre """
        return self.__nombre

    def obtener_interes_anual(self) :
        """ Obtiene interés anual """
        return self.__interes_anual 

    def obtener_deuda_actual(self) :
        """ Obtiene deuda actual """
        return self.__deuda_actual

    def obtener_pago(self) :
        """ Obtiene pago"""
        return self.__pago                

    def obtener_cargo(self) :
        """ Obtiene cargo """
        return self.__cargo

    def obtener_interes_mensual(self) :
        """ Obtiene interés mensual """
        return self.__interes_anual / 12
    
    def obtener_deuda_recalculada(self) :
        """ Obtiene deuda recalculada """
        deuda_recalculada = (self.obtener_deuda_actual() - self.obtener_pago())* (1 + (self.obtener_interes_mensual() / 100)) 
        return 0 if deuda_recalculada < 0 else deuda_recalculada

    def obtener_interes_mes(self) :
        """ Obtiene interes del mes """
        if self.obtener_deuda_recalculada() < 0 :
            return 0
        else :
            return (self.obtener_deuda_actual() - self.obtener_pago()) * (self.obtener_interes_mensual() / 100) 

    def obtener_deuda_despues_del_pago(self) :
        """ Obtiene deuda después del pago """
        deuda_despues_del_pago = self.obtener_deuda_actual() - self.obtener_pago()
        if deuda_despues_del_pago < 0 :
            return 0
        else : 
            return   deuda_despues_del_pago

    def obtener_nueva_deuda(self) :
        """ Obtiene nueva deuda """
        return self.obtener_deuda_recalculada() + self.obtener_cargo()
    
    def pago_recurrente(self) :
        """
        Genera los pagos recurrentes de una tarjeta hasta que no exista deuda.
        """
        while self.obtener_deuda_actual() > 0 :
            self.generar_reporte()
            self.asignar_deuda_actual(self.obtener_deuda_recalculada() + self.obtener_cargo()) 
            self.asignar_cargo(0)

    def obtener_pagos():
        """
        Obtiene la entrada de pagos diferentes
        """
        lista_pagos = []
        while True :
            pago : float = lee_numero("Escriba la cantidad del siguiente pago (Escriba 0 para terminar: ")
            if pago == 0 :
                return lista_pagos
            else :
                lista_pagos.append(pago)            
    
    def pagos_distintos(self) :
        """
        Genera los pagos distintos de una tarjeta
        """
        self.generar_reporte()
        pagos_list :list = obtener_pagos()

        for pago in pagos_list :
            self.asignar_pago(pago)
            self.asignar_deuda_actual(self.obtener_deuda_recalculada() + self.obtener_cargo()) 
            self.asignar_cargo(0)
            self.generar_reporte()

    def valida_pago(self,deuda) :
        """
        Obtiene una entrada en donde valida que no sea mayor a la deuda
        recibe como parámetro el valor de la deuda
        """
        while True :
            pago = float(lee_numero("Por favor digíte el pago a realizar: "))
            if  pago <= deuda :  
                return pago
            else :    
                print("el valor pagado: {:.2f} no puede ser  mayor que la deuda: {:.2f}".format(pago,deuda))            

    def generar_reporte(self) :
        """
        Genera el reporte de una tarjeta
        """
        #Resumen
        print("-"*100)
        print("-"*100)

        print("#"*45 +" Resumen "+ "#"*45)
        print("Tarjeta: {:>38}".format(self.obtener_nombre()))
        #print(f"Tasa de interes anual: {interes_anual_flt} % mensual: {interes_mensual_flt} %")
        print("Tasa de interes anual: {:>25.2f} % ".format(self.obtener_interes_anual()))
        print("-"*100)
        print("Deuda actual: {:>36.2f}".format(self.obtener_deuda_actual()))
        print("Pago: {:>44.2f}".format(self.obtener_pago()))
        print("-"*100)
        print("Deuda después del pago: {:>26.2f}".format(self.obtener_deuda_despues_del_pago()))
        print("Interés del mes: {:>33.2f}".format(self.obtener_interes_mes()))
        print("-"*100)
        print("Deuda recalculada: {:>31.2f}".format(self.obtener_deuda_recalculada()))
        print("Nuevos cargos: {:>35.2f}".format(self.obtener_cargo()))
        print("-"*100)
        print("Nueva deuda: {:>37.2f}".format(self.obtener_nueva_deuda()))
        print("#"*45 +" Fin de resumen "+ "#"*45)
        print()

    def capturar_tarjeta(self) :
        """
        Captura los datos de una tarjeta
        """
        print("#"*15 +" Ingresar datos "+ "#"*15)

        self.asignar_nombre(input("Por favor digite el nombre de la tarjeta: "))
        self.asignar_interes_anual(float(lee_numero("Por favor digíte la tasa de intéres: ")))
        self.asignar_deuda_actual(float(lee_numero("Por favor digíte la deuda actual del crédito: ")))
        self.asignar_pago(self.valida_pago(self.obtener_deuda_actual()))
        self.asignar_cargo(float(lee_numero("Por favor digíte el monto de los nuevos cargos: ")))
        
        print("#"*15 +" Fin de ingreso de datos "+ "#"*15)
        print()
    
    def guardar_tarjeta_json(self,archivo_salida) :
        """
        Guarda la información de la tarjeta en un archivo json
        """
        datos_dicts =[self.dict]
        
        with open(archivo_salida,"a") as arch_salida :
            json.dump(datos_dicts,arch_salida,indent = 4)
   
    def lee_tarjeta_json(self,archivo_entrada,tarjeta) :
        """
        Guarda la información de la tarjeta en un archivo json
        """        
        with open(archivo_entrada,"r") as arch_entrada :
            tarjetas = json.load(arch_entrada)
            for tarjeta in tarjetas :
                if tarjeta["nombre"] == tarjeta :
                    self.asignar_nombre(tarjeta["nombre"])
                    self.asignar_interes_anual(tarjeta["interes_anual"])
                    self.asignar_deuda_actual(tarjeta["deuda_actual"])
                    self.asignar_pago(tarjeta["pago"])
                    self.asignar_cargo(tarjeta["cargo"]) 

    def asigna_de_dict(self, tarjeta_dict) :
        """
        Asigna la información del la tarjeta de un dict
        """        
        self.asignar_nombre(tarjeta_dict["nombre"])
        self.asignar_interes_anual(tarjeta_dict["interes_anual"])
        self.asignar_deuda_actual(tarjeta_dict["deuda_actual"])
        self.asignar_pago(tarjeta_dict["pago"])
        self.asignar_cargo(tarjeta_dict["cargo"]) 

    def elimina_tarjeta_json(self,archivo_entrada,tarjeta) :
        """
        Guarda la información de la tarjeta en un archivo json
        """        
        with open(archivo_entrada,"r") as arch_entrada :
            tarjetas = json.load(arch_entrada)
            for tarjeta in tarjetas :
                if tarjeta["nombre"] == tarjeta :
                    self.asignar_nombre(tarjeta["nombre"])
                    self.asignar_interes_anual(tarjeta["interes_anual"])
                    self.asignar_deuda_actual(tarjeta["deuda_actual"])
                    self.asignar_pago(tarjeta["pago"])
                    self.asignar_cargo(tarjeta["cargo"]) 

    def decode_json(self, tarjeta_json):
        """ Pasa los datos de un json la objeto tarjeta """
        self.asignar_nombre(tarjeta_json["nombre"])
        self.asignar_interes_anual(tarjeta_json["interes_anual"])
        self.asignar_deuda_actual(tarjeta_json["deuda_actual"])
        self.asignar_pago(tarjeta_json["pago"])
        self.asignar_cargo(tarjeta_json["cargo"]) 

