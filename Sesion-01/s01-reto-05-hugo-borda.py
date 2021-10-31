def lee_numero(mensaje) :
    while True:
       entrada = input(mensaje)
       try:
           entrada = int(entrada)
           return entrada
       except ValueError:
           print("El dato ingresado no es numérico, por favor ingrese de nuevo la información.")

opcion_int = lee_numero(""" Elija una de las siguientes opciones para saber el precio del Helado
Digite 1 para Helado con oreo
Digite 2 para Helado con m&m
Digite 3 para Helado con fresas
Digite 4 para Helado con m&brownie: """)

if opcion_int == 1 :
    precio = 19
elif opcion_int == 2 :
    precio = 25
elif opcion_int == 3 :
    precio = 22
elif opcion_int == 4 :
    precio = 28
else :
    precio = -1

if precio == -1 :
    print("La opción de helado seleccionada no está disponible")
else :   
    print(f"El precio es: ${precio}")
