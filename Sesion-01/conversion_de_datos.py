# Se puede definir números como cadenas si se encierran en comillas
numero1 = "100"
numero2 = "3.14159"
print( type(numero1), type(numero1) )

# Para convertir a entero 
entero = int(numero1)
print( entero, type(entero) )

# Para convertir a flotante
flotante = float(numero2)
print( flotante,type(flotante) )

# También se puede convertir un número a cadena de texto
num = 300
cadena = str(num)
print( cadena, type(cadena))

# Leyendo una cadena
nombre = input("Dame tu nombre: ")
print( nombre, type(nombre) )

# Leyendo un entero
edad_str = input("Dame tu edad: ")
edad = int(edad_str)
print( edad, type(edad) )

edad_ = int(input("Dame tu edad: "))
print( edad, type(edad) )