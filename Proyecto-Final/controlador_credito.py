from utilidades.archivos import lista_archivos_json
from credito.usuario import Usuario
from credito.tarjeta import Tarjeta

RUTA_ARCHIVOS_JSON = "."

def get_usuarios() :
    """ Obtiene los usuarios """
    usuarios = []
    archivos_json = lista_archivos_json(RUTA_ARCHIVOS_JSON)
    for archivo_json in archivos_json :
        usuario = Usuario()
        usuario.asigna_json_a_usuario(archivo_json)
        usuarios.append(usuario)
    return usuarios

def get_usuario(usuario_) :
    """ Obtiene usuario dado su nombre"""
    usuarios = get_usuarios()
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario.nombre == usuario_:
            usuario_encontrado = usuario
            break
    return usuario_encontrado

def get_tarjeta(usuario_, tarjeta_) :
    """ Obtiene tarjeta dado su nombre y su usuario """
    usuario = get_usuario(usuario_)
    tarjeta_encontrada = None
    for tarjeta in usuario.tarjetas :
        if tarjeta.obtener_nombre() == tarjeta_:
            tarjeta_encontrada = tarjeta
            break
    return tarjeta_encontrada

def add_usuario(nombre):
    """ Adiciona usuario """
    usuario = Usuario(nombre)
    if (usuario.existe()) :
        return False
    else :
        usuario.guardar_json()
        return True

def del_usuario(nombre):
    """ Eliminar usuario """
    usuario = Usuario(nombre)
    usuario.eliminar_json()

def add_tarjeta_usuario(usuario, nombre, deuda, interes_anual, pago, cargo ):
    "Adiciona tarjeta a usuario "
    usuario = get_usuario(usuario)
    tarjeta =  Tarjeta(nombre,interes_anual,deuda,pago,cargo)      
    usuario.agregar_tarjeta_flask(tarjeta)

def del_tarjeta_usuario(usuario, tarjeta) :
    """Elimina tarjeta a usuairo """
    usuario = get_usuario(usuario)
    usuario.eliminar_tarjeta_flask(tarjeta)        
            