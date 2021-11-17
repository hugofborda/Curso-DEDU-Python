def lee_numero(mensaje) :
    while True:
       entrada = input(mensaje)
       try:
           entrada = float(entrada)
           return entrada
       except ValueError:
           print("El dato ingresado no es numérico, por favor ingrese de nuevo la información.")
      
def promedio(a,b) :
    """ Realiza el promedio de dos números """
    if a > 1000 or b > 1000:
        raise("Los valores son mayores de 1000")

    print(f"El promedio es: {(a+b)/2}")

def main() :
    """ Función principal """
    a = lee_numero("Digite el primer número: ")
    b = lee_numero("Digite el segundo número: ")

    try :
        promedio(a,b)
    except BaseException:
        print("Los valores son mayores de 1000")

main()
