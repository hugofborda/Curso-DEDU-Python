# Formas de declarar una lista vacia
lista_vacia = [] #Dentro de los corchetes se especifican los datos
lista_vacia2 = list() #Usando La función list


#Las listas pueden inicializarse con datos
lista_int = [1, 2, 3, 4, 5, 6, 7 ,8]
#            0  1  2  3  4  5  6  7
lista_fl = [1.4, 3.1415, 2.12, 12.7, 0.22]
lista_str = ['hola','mundo','!']
print(lista_int)
print(lista_fl)
print(lista_str)

# listas con diferentes tipos de datos

lista_mix =[4, 4.5, 'dos', lista_int, lista_fl]

print(lista_mix)

lista_list = [lista_vacia, lista_int, lista_fl, lista_mix]



print(lista_list)

# Operaciones
print(lista_int[0]) # elemento por índice
print(lista_int[2]) # primer índice 0 2 es el tercer elemento
print(len(lista_int)) # Cantidad de elementos
print(lista_int[len(lista_int) -1]) # último elemento
print(lista_int[-1]) # último elemento
print()
print("-"*40)
print()
# Obtener (slices)
print(lista_int[2:6]) # índice final una posición posterior (indice incial desde posición definida, índice final hasta elemento anterior)
print(lista_int[2:6:2]) # el último parámetro utiliza el salto de búsqueda en este caso de 2 en 2

print(lista_int[:6])
print(lista_int[2:])

print()
print("-"*40)
print()

lista_1 = []
lista_1.append(5) #5
print(lista_1)
lista_1.append(10) #10
print(lista_1)
lista_1.insert(0,1) # 1, 5, 10
print(lista_1)
lista_1.append(7) #1, 5 ,10, 7
print(lista_1)
lista_1.sort()
print(lista_1) # 1, 5, 7, 10

#Ordena lista de listas por el primer elemento si se repiten utiliza el siguiente elmento

# convertir cadenas en listas o listas en cadenas
texto = 'abdefg hijk'
lista =list(texto)
print(lista)
lista_2 = texto.split()
print(lista_2)

texto2 = "".join(lista) # abdefg hijk
texto3 = ".".join(lista) #a.b.d.e.f.g. .h.i.j.k
print(texto2)
print(texto3)
