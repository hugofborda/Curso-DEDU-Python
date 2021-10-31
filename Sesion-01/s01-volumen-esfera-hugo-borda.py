import math

def lee_numero(mensaje) :
    while True:
       entrada = input(mensaje)
       try:
           entrada = float(entrada)
           return entrada
       except ValueError:
           print("El dato ingresado no es numérico, por favor ingrese de nuevo la información.")


radio_flt = lee_numero("Escriba el radio de la esfera en km: ")

volumen_flt = (4 / 3) * math.pi * (radio_flt ** 3)

print("El volumen de la esfera es: {:.2f} km cúbicos".format(volumen_flt))