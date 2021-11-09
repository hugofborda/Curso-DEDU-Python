import math
from math import factorial, gcd as mcd

def lee_entero(mensaje) :
    while True:
       entrada = input(mensaje)
       try:
           entrada = int(entrada)
           return entrada
       except ValueError:
           print("El dato ingresado no es numérico, por favor ingrese de nuevo la información.")

print("#"*40)

x :int = lee_entero("Escriba el número para calcular la raíz cuadrada: ")
print(f"La raíz cuadrada de: {x} es: {math.sqrt(x)}")

print("#"*40)

x :int = lee_entero("Escriba el número a calcular el factorial: ")
print(f"El factorial de: {x} es: {factorial(x)}")

print("#"*40)

a :int = lee_entero("Escriba el primer número para obtener el mcd: ")
b :int = lee_entero("Escriba el segundo número para obtener el mcd: ")
print(f"El mcd de: {a} y {b} es: {mcd(a,b)}")