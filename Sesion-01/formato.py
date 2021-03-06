#Format sirve para añadir variables dentro de una cadena durante la ejecución
nombre = "Luis"  
print("Hola, mi nombre es {}".format(nombre)) #'Hola!, mi nombre es Luis'

#Incluso se pueden agregar variables que no son cadenas
edad = 28
print("Tengo {} años".format(edad))

#O se pueden agregar multiples datos
print("{} + {} = {}".format(4, 5, 4+5))  #4 + 5 = 9

# Añadir variables dentro de una cadena durante la ejecución
print( f"Hola, mi nombre es {nombre}" )

# Incluso se pueden agregar variables que no son cadenas
print( f"Tengo {edad} años" )

# O se pueden agregar multiples datos
print("{4} + {5} = {4+5}")