from credito.tarjeta import Tarjeta_de_credito as Tarjeta
import pytest

@pytest.mark.parametrize(
    "nombre_tarjeta, tasa, deuda, pago, cargo, nueva_deuda, deuda_recalculada"
    ,[
        ("Tarjeta1", 12 ,1200 ,200 ,100 ,1110 ,1010)
        ,("Tarjeta3", 14, 1400, 140, 40, 1314.7, 1274.7)
        ,("Maestro", 16, 1600, 160, 60, 1519.2, 1459.2)
        ,("Virtual", 12, 1200, 120, 100, 1190.8, 1090.8)
    ])
def test_calcula_nueva_deuda_mark(nombre_tarjeta, tasa, deuda, pago, cargo, nueva_deuda, deuda_recalculada) :
    """ Valida el cálculo de una nueva deuda """
    tarjeta = Tarjeta(nombre_tarjeta, tasa, deuda, pago, cargo)
    tarjeta.calcula_nueva_deuda()
    assert tarjeta.get_nueva_deuda() == nueva_deuda
    assert tarjeta.get_deuda_recalculada() == deuda_recalculada

def test_calcula_nueva_deuda() :
    """ Valida el cálculo de una nueva deuda """
    tarjeta = Tarjeta("Tarjeta1",12,1200,200,100)
    tarjeta.calcula_nueva_deuda()
    assert tarjeta.get_nueva_deuda() == 1110
    assert tarjeta.get_deuda_recalculada() == 1010

    tarjeta = Tarjeta("Tarjeta3",14,1400,140,40)
    tarjeta.calcula_nueva_deuda()
    assert tarjeta.get_nueva_deuda() == 1314.7
    assert tarjeta.get_deuda_recalculada() == 1274.7

    tarjeta = Tarjeta("Maestro",16,1600,160,60)
    tarjeta.calcula_nueva_deuda()
    assert tarjeta.get_nueva_deuda() == 1519.2
    assert tarjeta.get_deuda_recalculada() == 1459.2