from os.path import getsize, getmtime, join
from time import strftime, localtime

def obtener_informacion_archivo(ruta):
    """ Obtiene información del archivo definido en el parámetro ruta"""
    datos : tuple = ()
    tamanio = getsize(ruta) 
    fecha = getmtime(ruta)
    datos = (tamanio, fecha)

    return datos

def main():
    """ Función principal del programa"""
    arch = "Readme.md"
    ruta = join(".",arch)
    datos = obtener_informacion_archivo(ruta)
    fecha = localtime(datos[1])
    fecha = strftime("%d-%m-%Y %H:%M:%S",fecha)
    
    print(f"La última modificación de {arch} fue: {fecha}, tamaño: {datos[0]}")

main()