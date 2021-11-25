from sys import exit
from tarjeta.tarjeta import Tarjeta
from tarjeta.usuario import Usuario
from tarjeta.varios import borrar_terminal, lista_archivos_json
from tarjeta.entradas import lee_numero

usuarios = []

#Constantes
MENU_USUARIO = ((1,"Crear usuario"),
    (2,"Consultar usuarios"),
    (3,"Seleccionar usuario"),
    (4,"Salir"))

MENU_OPCIONES_USUARIO = ((1,"Adicionar tarjeta"),
    (2,"Imprimir tarjetas"),
    (3,"Eliminar tarjeta"),
    (4,"Regresar al menu de usuario"))

RUTA_ARCHIVOS_JSON = "."

def asigna_archivos_json_a_usuario() :
    """ Asigna los arhcivos json a objetos usuario """
    archivos_json = lista_archivos_json(RUTA_ARCHIVOS_JSON)
    for archivo_json in archivos_json :
        usuario = Usuario()
        usuario.asigna_json_a_usurio(archivo_json)
        usuarios.append(usuario)

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
    asigna_archivos_json_a_usuario()
    menu_usuario()
    
if __name__ == '__main__' :
    main()