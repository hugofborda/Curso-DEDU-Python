# Leyendo una cadena

def lee_numero(mensaje) :
    while True:
       entrada = input(mensaje)
       try:
           entrada = float(entrada)
           return entrada
       except ValueError:
           print("El dato ingresado no es numérico, por favor ingrese de nuevo la información.")

def lee_S_N(mensaje) :
    while True:
        entrada_str = input(mensaje)
        if entrada_str.lower() == 's' or entrada_str.lower() == 'n' :
           return entrada_str
        else :
            print("La opción digitada no es S o N.")

def valida_pago(deuda) :
    while True :
        pago = float(lee_numero("Por favor digíte el pago a realizar: "))
        if  pago <= deuda :  
            return pago
        else :    
            print("el valor pagado: {:.2f} no puede ser  mayor que la deuda: {:.2f}".format(pago,deuda))

def crear_tarjeta() :
    #Ingreso de datos
    print("#"*50 +" Ingresar datos "+ "#"*50)

    tarjeta_dict :dict = dict()

    tarjeta_dict["nombre"] = input("Por favor digite el nombre del dueño de la tarjeta: ")
    tarjeta_dict["interes_anual"] = float(lee_numero("Por favor digíte la tasa de intéres: "))
    tarjeta_dict["deuda_actual"] = float(lee_numero("Por favor digíte la deuda actual del crédito: "))
    tarjeta_dict["pago"] = valida_pago(tarjeta_dict["deuda_actual"])
    tarjeta_dict["cargo"] = float(lee_numero("Por favor digíte el monto de los nuevos cargos: "))
    
    print("#"*40 +" Fin de ingreso de datos "+ "#"*40)
    print()
    return tarjeta_dict

def captura_nueva_deuda(tarjeta_dict) :
    #Cálculos
    tarjeta_dict["interes_mensual"] = tarjeta_dict["interes_anual"] / 12
    tarjeta_dict["deuda_recalculada"] = (tarjeta_dict["deuda_actual"] - tarjeta_dict["pago"]) * (1 + (tarjeta_dict["interes_mensual"] / 100)) 
    tarjeta_dict["interes_mes"] = (tarjeta_dict["deuda_actual"] - tarjeta_dict["pago"]) * (tarjeta_dict["interes_mensual"] / 100) 

    if  tarjeta_dict["deuda_recalculada"] < 0 : 
        tarjeta_dict["deuda_recalculada"] = 0
        tarjeta_dict["interes_mes"] = 0

    return tarjeta_dict

def generar_reporte(tarjeta_dict) :
    #Resumen
    print("-"*100)
    print("-"*100)

    print("#"*45 +" Resumen "+ "#"*45)
    print("Tarjeta de: {:>38}".format(tarjeta_dict["nombre"]))
    #print(f"Tasa de interes anual: {interes_anual_flt} % mensual: {interes_mensual_flt} %")
    print("Tasa de interes anual: {:>25.2f} % ".format(tarjeta_dict["interes_anual"] ))
    print("-"*100)
    print("Deuda actual: {:>36.2f}".format(tarjeta_dict["deuda_actual"]))
    print("Pago: {:>44.2f}".format(tarjeta_dict["pago"]))
    print("-"*100)
    deuda_despues_del_pago = tarjeta_dict["deuda_actual"] - tarjeta_dict["pago"]
    if deuda_despues_del_pago < 0 :
        deuda_despues_del_pago = 0
    print("Deuda después del pago: {:>26.2f}".format(deuda_despues_del_pago))
    print("Interés del mes: {:>33.2f}".format(tarjeta_dict["interes_mes"]))
    print("-"*100)
    print("Deuda recalculada: {:>31.2f}".format(tarjeta_dict["deuda_recalculada"]))
    print("Nuevos cargos: {:>35.2f}".format(tarjeta_dict["cargo"]))
    print("-"*100)
    print("Nueva deuda: {:>37.2f}".format(tarjeta_dict["deuda_recalculada"] + tarjeta_dict["cargo"]))
    print("#"*45 +" Fin de resumen "+ "#"*45)
    print()

def crear_tarjetas() :
    tarjetas_list = []
    while True :
        tarjetas_list.append(crear_tarjeta())
        opcion = lee_S_N("Desea ingresar una nueva tarjeta, digite S o N: ")
        if  opcion.lower() == 'n' :
            return tarjetas_list

def generar_reportes(tarjetas_list) :
    for tarjeta_dict in tarjetas_list :
        captura_nueva_deuda(tarjeta_dict)
        generar_reporte(tarjeta_dict)

def pago_recurrente(tarjeta_dict) :
    tarjeta_dict_copia = tarjeta_dict.copy()
    while tarjeta_dict_copia["deuda_actual"] > 0 :
        captura_nueva_deuda(tarjeta_dict_copia)
        generar_reporte(tarjeta_dict_copia)
        tarjeta_dict_copia["deuda_actual"] = tarjeta_dict_copia["deuda_recalculada"] + tarjeta_dict_copia["cargo"]
        tarjeta_dict_copia["cargo"] = 0

def main() :
    """ Función principal"""
    tarjetas_list = []
    tarjetas_list = crear_tarjetas()
    #generar_reportes(tarjetas_list)
    pago_recurrente(tarjetas_list[0])
    
main()



