def lee_numero(mensaje) :
    while True:
       entrada = input(mensaje)
       try:
           entrada = int(entrada)
           return entrada
       except ValueError:
           print("El dato ingresado no es numérico, por favor ingrese de nuevo la información.")

def obtener_mcm_inicial(a,b) :
    if a % b == 0 :
        return a
    elif b % a == 0 :
        return b
    elif a > b :
        return a
    else :
        return b

def es_mcm(d,a,b) :
    if (d % a == 0) and (d % b == 0) :
        return True
    else :
        return False

def obtener_mcm(a,b) :
    d :int = obtener_mcm_inicial(a,b)
    while es_mcm(d,a,b) == False :
        d += 1
    return d

print("#"*60)
print("Cálculo de mínimo común múltiplo para dos números")
print("#"*60)
a :int = lee_numero("Por favor ingrese el primer número: ")
b :int = lee_numero("Por favor ingrese el segundo número: ")
print("#"*60)
d = obtener_mcm(a,b)


print(f"El m.c.m de {a} y {b} es: {d}")


