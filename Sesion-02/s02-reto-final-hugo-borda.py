def lista_ordenada_sin_repetidos(lista_parametro) :
    lista_sin_duplicados = list(set(lista_parametro))
    lista_sin_duplicados.sort()
    for x in lista_sin_duplicados :
        print(x)

    return lista_sin_duplicados
    
  
lista = [5,7,9,11,23,1,3,4,45,12,23,32,12,11,45,57,11,23,607]

print("la lista resultante es: {}".format(lista_ordenada_sin_repetidos(lista)))