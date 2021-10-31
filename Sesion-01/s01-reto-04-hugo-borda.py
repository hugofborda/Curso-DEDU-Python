def lee_numero(mensaje) :
    while True:
       entrada = input(mensaje)
       try:
           entrada = int(entrada)
           return entrada
       except ValueError:
           print("El dato ingresado no es numérico, por favor ingrese de nuevo la información.")

tabla_int = lee_numero("Digite el número de la tabla que desea generar: ")          

for x in range(1,11) :
    print("{:>2} x {:>2} = {:>2}".format(x,tabla_int,x * tabla_int))