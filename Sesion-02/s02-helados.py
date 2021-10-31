def lee_numero(mensaje) :
    while True:
       entrada = input(mensaje)
       try:
           entrada = int(entrada)
           return entrada
       except ValueError:
           print("El dato ingresado no es numérico, por favor ingrese de nuevo la información.")

menu = ((1,"Helado con oreo",19),
(2,"Helado con m&m",25),
(3,"Helado con fresas",22),
(4,"Helado con m&brownie",28),
)
print("#"*40)
for x in menu:
    print(f"{x[0]} {x[1]}")
print("#"*40)

opcion_int = lee_numero("Seleccione la opción: ")

if opcion_int > 0 and opcion_int < len(menu) :
    precio = menu[opcion_int][2]
else :
    precio = -1

if precio == -1 :
    print("La opción de helado seleccionada no está disponible")
else :   
    print(f"El precio es: ${precio}")
