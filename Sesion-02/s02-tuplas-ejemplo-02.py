# Formas de declarar una tupla vacia
tupla_vacia = () #Dentro de los corchetes se especifican los datos
tupla_vacia2 = tuple() #Usando La función list


#Las tuplas pueden inicializarse con datos
tupla_int = (1, 2, 3, 4, 5, 6, 7 ,8)
#            0  1  2  3  4  5  6  7
tupla_fl = (1.4, 3.1415, 2.12, 12.7, 0.22)
tupla_str = ('hola','mundo','!')
print(tupla_int)
print(tupla_fl)
print(tupla_str)

# tuplas con diferentes tipos de datos

tupla_mix =(4, 4.5, 'dos', tupla_int, tupla_fl)

print(tupla_mix)

tupla_list = (tupla_vacia, tupla_int, tupla_fl, tupla_mix)



print(tupla_list)

# Operaciones
print(tupla_int[0]) # elemento por índice
print(tupla_int[2]) # primer índice 0 2 es el tercer elemento
print(len(tupla_int)) # Cantidad de elementos
print(tupla_int[len(tupla_int) -1]) # último elemento
print(tupla_int[-1]) # último elemento
print()
print("-"*40)
print()
# Obtener (slices)
print(tupla_int[2:6]) # índice final una posición posterior (indice incial desde posición definida, índice final hasta elemento anterior)
print(tupla_int[2:6:2]) # el último parámetro utiliza el salto de búsqueda en este caso de 2 en 2

print(tupla_int[:6])
print(tupla_int[2:])

print()
print("-"*40)
print()

# convertir cadenas en tuplas o tuplas en cadenas
texto = 'abdefg hijk'
tupla =tuple(texto)
print(tupla)

texto2 = "".join(tupla) # abdefg hijk
texto3 = ".".join(tupla) #a.b.d.e.f.g. .h.i.j.k
print(texto2)
print(texto3)

lista = list(tupla)
lista.sort()
print(list)