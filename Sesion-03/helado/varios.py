import os

# Definición de funciones
def borrar_terminal():
    """ Borra la terminal """
    if os.name == 'posix' :
        os.system("clear")  # Linux y Mac
    else :
        os.system("cls")  # Windows

menu = (
    (1, "Helado con oreo"),     # 0
    #0  1
    (2, "Helado con m&m"),      # 1
    (3, "Helado con fresas"),   # 2
    (4, "Helado con brownie"),  # 3
)
