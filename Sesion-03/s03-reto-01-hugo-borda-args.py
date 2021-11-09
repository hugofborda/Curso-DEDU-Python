def try_cast_float(arg) :
    try:
        arg = float(arg)
        return arg
    except ValueError:
        return 0

def imprimir_argumentos(*args) :
    a : float = 0
    for arg in args :
        a += try_cast_float(arg)
    return a

def imprimir_directorio(**kwargs) :
    kwargs : dict = dict(kwargs)
    kwargs_sorted = sorted(kwargs)
    for key in kwargs_sorted :
        print("El número de teléfono de: {:8} es: {:>8}".format(key,kwargs[key]))

def main() :
    suma = imprimir_argumentos(1, 2, 3, 4, 'a', 5, 6, 7)
    print(f"la suma de valores es: {suma}")
    print()
    imprimir_directorio( Juan = 1111111, Andrea = 2222222, Luisa = 3333333, Pedro = 4444444, Alicia = 5555555)

main()