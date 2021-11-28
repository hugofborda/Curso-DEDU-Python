""" Modulo para manejar archivos """
from os import listdir, path, remove

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

def existe_archivo(ruta) :
    """ Valida existencia de archivo """
    return path.isfile(ruta)

def eliminar_archivo(ruta) :
    """ Valida existencia de archivo """
    if path.isfile(ruta) :
        remove(ruta)
