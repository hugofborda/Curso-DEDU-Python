import os
import click
import csv
import time

class Archivo() :
    def __init__(self, ruta) :
        """ Crea objeto Archivo a partir de ruta """
        self.__ruta = ruta
        try :
            self.tamanio = os.path.getsize(ruta) # arch -> ls.py
            self.fecha = os.path.getmtime(ruta)
        except FileNotFoundError :
            pass
        except OSError :
            pass
        

    @property #Cambia el método como una propiedad y no recibe parámetros se llama sin paréntesis
    def get_ruta(self) :
        return self.__ruta

    def __str__(self) -> str:
        """ Define la representación en str de Archivo"""
        return self.__ruta

    @property    
    def fecha_str(self) :
        """ Reperesentación en cadena del atributo fecha """
        fecha : tuple = time.localtime(self.fecha)
        fecha : str = time.strftime("%d-%m-%Y %H:%M:%S",fecha)
        return fecha
    
    def texto(self) -> str :
        " Representación en texto deplano de un archivo "
        #fecha : tuple = time.localtime(self.fecha)
        #fecha : str = time.strftime("%d-%m-%Y %H:%M:%S",fecha)
        #return f"{self.tamanio:10} {fecha:19} {self.__ruta}"
        return f"{self.tamanio:10} {self.fecha_str():19} {self.__ruta}"

    @property
    def tupla_str(self) :
        """ Representación en tupla de un ARchivo con fecha en cadena"""
        return (self.tamanio, self.fecha_str, self.get_ruta)
        

class Carpeta(Archivo) :
    def lista_elementos(self, ) :
        """ Obtiene la lista de elementos de la carpeta """
        try :
            archivos :list = os.listdir(self.get_ruta) # archviso => ["uno.py", "dos.py",]
        except PermissionError :
            archivos :list = []
        # elementos [Archivo("uno.py"),Archivo("dos.py"), Carpeta("c:/")]    
        elementos = []
        for arch in archivos :
            # arch -> ruta +"uno.py, datos"
            ruta = os.path.join(self.get_ruta,arch) # "c:/python/ruta"
            if os.path.isdir(ruta) :
                carpeta = Carpeta(ruta)
                elementos.append( carpeta )
                elementos += carpeta.lista_elementos()
            else :
                elementos.append( Archivo(ruta) )
        return elementos
    
    def texto(self) -> str:
        return super().texto() + "\\"
    
#Modelo
def obtener_lista(carpeta):
    """
    Regresa la lista de los archivos de la carpeta
    """
    lista= os.listdir(carpeta)
    # [(23432, "dd-mm-yyyy hh:mm:ss", "ls.py"), (23345, "dd-mm-yyyy hh:mm:ss", "ls.py1")]
    datos = []
    for arch in lista :
        ruta = os.path.join(carpeta,arch)
        tamanio = os.path.getsize(ruta) # arch -> ls.py
        fecha = os.path.getmtime(ruta)
        datos.append((tamanio, fecha, arch))
    return datos

#Vista
def imprime_en_texto(lista):
    """ Imprime los elementos de la lista en la salida estándar en formato texto plano """
    for arch in lista: # lista -> [Archivo(),Carpeta(),Archivo()]
        print(arch.texto())

def guarda_en_archivo(lista, ruta):
    """ Guarda los elementos de la lista en el archivo 'ruta' en formato texto plano """
    with open(ruta,"w", encoding = "utf-8") as arch_texto: # default utf-8m iso8859-1, latin-1
        for elemento in lista: # lista -> [Archivo(),Carpeta(),Archivo()]
            arch_texto.write(elemento.texto())
            arch_texto.write("\n")

def guarda_en_archivo_csv(lista, ruta):
    """ Guarda los elementos de la lista en el archivo 'ruta' en formato csv """
    with open(ruta,"w", encoding = "utf-8", newline="\n") as arch_texto: # default utf-8m iso8859-1, latin-1
        escritor_csv = csv.writer(arch_texto, delimiter=";") # , newline="\n" validar
        for elemento in lista: # lista -> [Archivo(),Carpeta(),Archivo()]    
           # arch_texto.write(elemento.texto())
           # arch_texto.write("\n")      
           escritor_csv.writerow(elemento.tupla_str)

#Controlador
@click.command()
@click.argument("carpeta", default=".", type=click.Path(exists=True))
@click.option("--csv","salida_csv", is_flag=True, 
                help="Guarda los resultados en formato csv") #Opciones de línea de comando, se renombra csv para que se renombre la entrada del comando, con flag se regresa al escribir la opción csv como true, en caso contrario false en la variable salida_csv
def main(carpeta, salida_csv) :
    """
    Lista los archivos y carpetas de la carpeta actual o de sus subcarpetas
    """
    carpeta_obj = Carpeta(carpeta)
    elementos :list = carpeta_obj.lista_elementos()
   
    if salida_csv :
        guarda_en_archivo_csv(elementos, "salida.csv")
    else :    
        #imprime_en_texto(elementos)
        guarda_en_archivo(elementos, "salida.txt")
    

if __name__ == '__main__' :
    main()
