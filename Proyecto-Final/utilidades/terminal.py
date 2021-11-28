""" Modulos para manejo de terminal """
from os import name, system

def borrar_terminal():
    """ Borra la terminal """
    if name == 'posix' :
        system("clear")  # Linux y Mac
    else :
        system("cls")  # Windows

