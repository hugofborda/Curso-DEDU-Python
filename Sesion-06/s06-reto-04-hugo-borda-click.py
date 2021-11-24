import click

@click.command()
@click.argument("archivo", type=click.File("r"))
@click.argument("linea", default=1, type=int)
def main(archivo,linea) :
    lineas =archivo.readlines()
    if len(lineas) > linea :
        print(lineas[linea])
    else :
        print(f"El archivo no posee la línea: {linea}")


if __name__ == '__main__' :
    main()
