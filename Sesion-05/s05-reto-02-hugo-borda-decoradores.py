def decorador(f):
    """ Función decorador"""
    def nueva_funcion() :
        f()
        f()
        f()
    return nueva_funcion
    
@decorador
def decorada() :
    """ Función decorada """
    print("Hola")

def main():
    """ Función principal """
    decorada()

main()
