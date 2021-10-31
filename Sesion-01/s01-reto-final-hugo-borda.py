def lee_numero(mensaje) :
    while True:
       entrada = input(mensaje)
       try:
           entrada = float(entrada)
           return entrada
       except ValueError:
           print("El dato ingresado no es numérico, por favor ingrese de nuevo la información.")

numero1_flt = lee_numero("Por favor digite el primer número: ")
numero2_flt = lee_numero("Por favor digite el segundo número: ")

operador_str = input("Por favor digite el operador a utilizar: ")

if operador_str == '+' :
    print(f"{numero1_flt} + {numero2_flt} = {numero1_flt + numero2_flt}")
elif operador_str == '-' :
    print(f"{numero1_flt} - {numero2_flt} = {numero1_flt - numero2_flt}")
elif operador_str == '*' :
    print(f"{numero1_flt} * {numero2_flt} = {numero1_flt * numero2_flt}")
elif operador_str == '/' and numero2_flt != 0 :   
    print(f"{numero1_flt} / {numero2_flt} = {numero1_flt / numero2_flt}")
elif operador_str == '/' and numero2_flt == 0 :   
    print("División por 0")
else :
    print("El operador no es valido o no está configurado")        
    
    

