import datos.bd as bd
from credito.usuario import Usuario
from credito.tarjeta import Tarjeta

def get_usuarios() :
    """ Obtiene los usuarios """
    usuarios = bd.session.query(Usuario).all()
    for usuario in usuarios :
        tarjetas = bd.session.query(Tarjeta).filter(Tarjeta.usuario == usuario.nombre).all()
        usuario.asignar_tarjetas(tarjetas)
    return usuarios

def get_usuario(usuario_) :
    """ Obtiene usuario dado su nombre"""
    usuario = bd.session.query(Usuario).get(usuario_)
    if usuario != None :
        tarjetas = bd.session.query(Tarjeta).filter(Tarjeta.usuario == usuario.nombre).all()
        if tarjetas != None :
            usuario.asignar_tarjetas(tarjetas)
    return usuario

def get_tarjeta(usuario_, tarjeta_) :
    """ Obtiene tarjeta dado su nombre y su usuario """
    tarjeta = bd.session.query(Tarjeta).filter(Tarjeta.usuario == usuario_ and Tarjeta.nombre == tarjeta_).first()
    return tarjeta

def add_usuario(usuario_):
    """ Adiciona usuario """
    usuario = get_usuario(usuario_)
    if (usuario != None) :
        return False
    else :
        usuario = Usuario(usuario_)
        bd.session.add(usuario)
        bd.session.commit()
        return True

def del_usuario(usuario_):
    """ Eliminar usuario """
    bd.session.query(Usuario).filter(Usuario.nombre == usuario_).delete()
    bd.session.commit()

def add_tarjeta_usuario(usuario, nombre, deuda, interes_anual, pago, cargo ):
    "Adiciona tarjeta a usuario "
    tarjeta =  Tarjeta(nombre,interes_anual,deuda,pago,cargo,usuario)      
    bd.session.add(tarjeta)
    bd.session.commit()

def del_tarjeta_usuario(usuario_, tarjeta_) :
    """Elimina tarjeta a usuairo """
    bd.session.query(Tarjeta).filter(Tarjeta.usuario == usuario_ and Tarjeta.nombre == tarjeta_).delete()
    bd.session.commit()

def inicializa_bd() :
    bd.Base.metadata.create_all(bd.engine)
            