from sys import exit
from credito.usuario import Usuario
from utilidades.entradas import lee_numero
from utilidades.terminal import borrar_terminal
from controlador_credito import get_usuarios

#Constantes
MENU_USUARIO = ((1,"Crear usuario"),
    (2,"Consultar usuarios"),
    (3,"Seleccionar usuario"),
    (4,"Salir"))

MENU_OPCIONES_USUARIO = ((1,"Adicionar tarjeta"),
    (2,"Imprimir tarjetas"),
    (3,"Eliminar tarjeta"),
    (4,"Regresar al menu de usuario"))

usuarios = get_usuarios()

def capturar_usuario():
    """ Captura un nuevo usuario """
    nombre :str = input("Digíte el nombre del usuario: ")
    usuario = Usuario(nombre)
    usuarios.append(usuario)
    return usuario

def listar_usuarios():
    """ lista los usuarios """
    print("#"*15 + " Usuarios " + "#"*15)
    if len(usuarios) == 0 :
        print("No exiten usuarios creados.")
    else         :
        for usuario in usuarios:
            print(f"Usuario: {usuario.nombre:20}")
    print("#"*30)

def seleccionar_usuario() :
    """ Selecciona un usuario """
    nombre = input("Digite el nombre del usuario: ")
    encontrado = None
    for usuario in usuarios :
        if usuario.nombre.lower() == nombre.lower() :
            encontrado = usuario
    if encontrado != None :
        borrar_terminal()
        menu_opciones_usuario(encontrado)
    else :
        print(f"El usuario {nombre}, no existe")        
        menu_usuario()
    
def imprimir_menu(menu) :
    """ Imprime la lista de opciones de tarjetas """
    print("#"*30)
    for x in menu:
        print(f"{x[0]} {x[1]}")
    print("#"*30)

def menu_usuario() :
    """ Función de selección de menú de usuario """
    imprimir_menu(MENU_USUARIO)
    opcion :int = lee_numero("Seleccione la opción: ")

    if opcion == 1 :
        usuario = capturar_usuario()
        borrar_terminal()
        menu_opciones_usuario(usuario)
    if opcion == 2 :
        borrar_terminal()
        listar_usuarios()
        menu_usuario()
    if opcion == 3 :
        borrar_terminal()
        seleccionar_usuario()
    if opcion == 4 :
        exit()        
    else :
        print("La opcion seleccionada no es valida")
        menu_usuario()

def menu_opciones_usuario(usuario) :
    """ Función de selección de menú de opciones de usuario """
    imprimir_menu(MENU_OPCIONES_USUARIO)
    print( f"###   {usuario.nombre} ###")
    opcion :int = lee_numero("Seleccione la opción: ")

    if opcion == 1 :
        usuario.agregar_tarjeta()
        menu_opciones_usuario(usuario)
    if opcion == 2 :
        usuario.imprimir_tarjetas()
        menu_opciones_usuario(usuario)
    if opcion == 3 :
        usuario.eliminar_tarjeta()
        menu_opciones_usuario(usuario)        
    if opcion == 4 :
        borrar_terminal()
        menu_usuario()
    else :
        print("La opcion seleccionada no es valida")
        menu_opciones_usuario(usuario) 

def main() :
    """ Programa principal """
    borrar_terminal()
    menu_usuario()
    
if __name__ == '__main__' :
    main()