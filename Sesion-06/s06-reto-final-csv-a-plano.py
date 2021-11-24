# 1 Leer la información de la línea de comando: nobre de archivo
# 2 Crear el nombre del archivo de salida
# 3 Leer los archivos de csv
# 4 Escrubir los datos en el archivo json
# 4.1 Obtener los nombres de las columnas

import click
import csv
import json
import os

def lee_csv(archivo):
    """ Leer los registros del archivo csv y regresa una lista """
    with open(archivo,"r") as arch :
        csv_lector = csv.reader(arch, delimiter=",")
        # datos = []
        # for fila in csv_lector
        #   datos.append(fila)
        datos = list(csv_lector)
        #[
        #    (col1,col2,col3,....),
        #    [col1,col2,col3,....],
        #    (col1,col2,col3,....),
        #]
    return datos


def escribe_json(archivo_salida,datos) :
    """ Escrile los datos en archivo_salida en formato JSON"""
    etiquetas = datos[0]
    datos_dicts =[]
    for fila in datos[1:] :
        fila_dict = {}
        for (i,etiqueta) in enumerate(etiquetas): 
            fila_dict[etiqueta] = fila[i]
        datos_dicts.append(fila_dict)

    with open(archivo_salida,"w") as arch_salida :
        #arch_salida.write(json.dumps(datos_dicts))
        json.dump(datos_dicts,arch_salida,indent =4)

def escribe_texto(archivo_salida,datos) :
    """ Escrile los datos en archivo_salida en formato texto"""
    etiquetas = ["Nombre","Edad","Ciudad"]
    with open(archivo_salida,"w") as arch_salida :
        for fila in datos :
            fila_str =""
            for (i,etiqueta) in enumerate(etiquetas) :
                fila_str += f"{etiqueta}: {fila[i].strip()} "
            arch_salida.write(fila_str +"\n")

#Controlador
@click.command()
@click.argument("archivo", type=click.Path(exists=True))
def main(archivo) :
    """
    Convierte archivo CSV a JSON
    """    
    print(archivo)
    #archivo_salida = archivo.split(".")[0] + '.json' # ['salida','csv]
    datos = lee_csv(archivo)
    #archivo_salida = os.path.splitext(archivo)[0] + '.json'
    #escribe_json(archivo_salida, datos)
    archivo_salida = os.path.splitext(archivo)[0] + '.txt'
    escribe_texto(archivo_salida, datos)
    print(archivo_salida)
if __name__ == '__main__' :
    main()
