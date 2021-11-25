from os import name, system, listdir, path

def borrar_terminal():
    """ Borra la terminal """
    if name == 'posix' :
        system("clear")  # Linux y Mac
    else :
        system("cls")  # Windows

def lista_archivos_json(ruta) :
        """ Obtiene la lista de elementos de la carpeta """
        try :
            archivos :list = listdir(ruta) # archviso => ["uno.py", "dos.py",]
        except PermissionError :
            archivos :list = []
        # elementos [Archivo("uno.py"),Archivo("dos.py"), Carpeta("c:/")]    
        elementos = []

        for arch in archivos :
            # arch -> ruta +"uno.py, datos"
            ruta_archivo = path.join(ruta,arch) # "c:/python/ruta"
            if path.isfile(ruta_archivo) and arch.endswith("_tarjeta.json"):
                elementos.append(ruta_archivo)
        return elementos