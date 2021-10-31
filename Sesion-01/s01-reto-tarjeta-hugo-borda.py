# Leyendo una cadena

def lee_numero(mensaje) :
    while True:
       entrada = input(mensaje)
       try:
           entrada = float(entrada)
           return entrada
       except ValueError:
           print("El dato ingresado no es numérico, por favor ingrese de nuevo la información.")

def valida_pago(deuda) :
    while True :
        pago = float(lee_numero("Por favor digíte el pago a realizar: "))
        if  pago <= deuda :  
            return pago
        else :    
            print("el valor pagado: {:.2f} no puede ser  mayor que la deuda: {:.2f}".format(pago,deuda))

#Ingreso de datos
print("-"*40 +"Ingresar datos"+ "-"*40)
nombre_str = input("Por favor digite el nombre del dueño de la tarjeta: ")
interes_anual_flt = float(lee_numero("Por favor digíte la tasa de intéres: "))
deuda_actual_flt = float(lee_numero("Por favor digíte la deuda actual del crédito: "))
pago_flt = valida_pago(deuda_actual_flt)
nuevo_cargo_flt = float(lee_numero("Por favor digíte el monto de los nuevos cargos: "))

#Cálculos
interes_mensual_flt = interes_anual_flt/12
deuda_recalculada_flt = (deuda_actual_flt - pago_flt) * (1 + (interes_mensual_flt / 100)) 
interes_mes_flt= (deuda_actual_flt - pago_flt) * (interes_mensual_flt / 100) 


#Resumen
print("-"*100)
print("-"*100)

print("-"*45 +"Resumen"+ "-"*45)
print("Tarjeta de: {:>38}".format(nombre_str))
#print(f"Tasa de interes anual: {interes_anual_flt} % mensual: {interes_mensual_flt} %")
print("Tasa de interes anual: {:>25.2f} % ".format(interes_anual_flt))
print("-"*100)
print("Deuda actual: {:>36.2f}".format(deuda_actual_flt))
print("Pago: {:>44.2f}".format(pago_flt))
print("-"*100)
print("Deuda después del pago: {:>26.2f}".format(deuda_actual_flt - pago_flt))
print("Interés del mes: {:>33.2f}".format(interes_mes_flt))
print("-"*100)
print("Deuda recalculada: {:>31.2f}".format(deuda_recalculada_flt))
print("Nuevos cargos: {:>35.2f}".format(nuevo_cargo_flt))
print("-"*100)
print("Nueva deuda: {:>37.2f}".format(deuda_recalculada_flt + nuevo_cargo_flt))
print("-"*100)
print("-"*100)

