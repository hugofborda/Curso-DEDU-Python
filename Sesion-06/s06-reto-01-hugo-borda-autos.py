import os

def lee_numero(mensaje) :
    """
    Obtiene una entrada estándar la cual valida que sea un número
    recibe un parámetro de entrada que indica el mensaje a mostrar en la entrada.
    """
    while True:
       entrada = input(mensaje)
       try:
           entrada = float(entrada)
           return entrada
       except ValueError:
           print("El dato ingresado no es numérico, por favor ingrese de nuevo la información.")

class Auto():
    """ Clase que define auto """
    __EQUIPAMIENTOS =["bajo", "medio", "alto"]

    def __init__(self) -> None:
        self.nombre = None
        self.color = None
        self.nivel_equipamiento = None
        self.precio = None

    def __str__(self) -> str:
        return f"{self.nombre:50} {self.color:50} {self.nivel_equipamiento :20} {self.precio:20}"        

    def lee_equipamiento(self) :
        """ Obtiene el equipamiento del vehículo """
        while True:
            entrada = input("Equipamiento del vehículo"+ ",".join(self.__EQUIPAMIENTOS)+": ")
            if entrada in self.__EQUIPAMIENTOS :
                return entrada
            else :
                print("El equipamiento debe ser: " + ",".join(self.__EQUIPAMIENTOS))

    def guarda_en_archivo(self, ruta):
        """ Guarda la información del auto en un archivo """
        with open(ruta,"a") as arch_texto:
            arch_texto.write(self.__str__())
            arch_texto.write("\n")
        print("#"*100)
        print("#"*40 +f" Datos almacenados a {ruta} "+ "#"*40)
        print("#"*100)
        
        

    def capturar_datos(self) :
        """ Captura datos de auto """
        print("#"*50 +" Ingresar datos "+ "#"*50)
        self.nombre = input("Nombre del vehículo: ")
        self.color = input("Color del vehículo: ")
        self.nivel_equipamiento = self.lee_equipamiento()
        self.precio = lee_numero("Precio del vehículo: ")
        print("#"*40 +" Fin de ingreso de datos "+ "#"*40)

def main() :
    """ Programa principal """
    auto = Auto()
    auto.capturar_datos()
    auto.guarda_en_archivo("autos.txt")

if __name__ == '__main__' :
    main()
