from credito.usuario import Usuario
import pytest


@pytest.mark.parametrize(
    "usuario, respuesta"
    ,[
        ("Juan", True)
        ,("Andrea", True)
        ,("Alicia",False)
        ,("Camila", False)
    ])
def test_existe(usuario, respuesta) :
    """ Valida exitencia de archivo de usuario """
    usuario = Usuario(nombre=usuario)
    assert type(usuario.existe()) == bool
    assert usuario.existe() == respuesta

@pytest.mark.parametrize(
    "usuario, respuesta"
    ,[
        ("Juan", "Juan_tarjeta.json")
        ,("Andrea", "Andrea_tarjeta.json")
        ,("Alicia","Alicia_tarjeta.json")
        ,("Camila", "Camila_tarjeta.json")
    ])

def test_nombre_archivo(usuario, respuesta) :
    """ Valida nombre de archivo json de datos de usuario """
    usuario = Usuario(nombre=usuario)
    assert type(usuario.nombre_archivo) == str
    assert len(usuario.nombre_archivo) > 0
    assert usuario.nombre_archivo == respuesta    
