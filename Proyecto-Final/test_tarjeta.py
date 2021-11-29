from credito.tarjeta import Tarjeta
import pytest

@pytest.mark.parametrize(
    "nombre_tarjeta, tasa, deuda, pago, cargo, nueva_deuda, deuda_recalculada, interes_mes"
    ,[
        ("Tarjeta1", 12 ,1200 ,200 ,100 ,1110 ,1010, 10)
        ,("Tarjeta3", 14, 1400, 140, 40, 1314.7, 1274.7, 14.7)
        ,("Maestro", 16, 1600, 160, 60, 1519.2, 1459.2, 19.2)
        ,("Virtual", 12, 1200, 120, 100, 1190.8, 1090.8, 10.8)
    ])
def test_calcula_nueva_deuda_mark(nombre_tarjeta, tasa, deuda, pago, cargo, nueva_deuda, deuda_recalculada, interes_mes) :
    """ Valida el cálculo de una nueva deuda """
    tarjeta = Tarjeta(nombre_tarjeta, tasa, deuda, pago, cargo)    
    assert type(tarjeta.obtener_nueva_deuda()) == float
    assert type(tarjeta.obtener_deuda_recalculada()) == float
    assert type(tarjeta.obtener_interes_mensual()) == float
    assert type(tarjeta.obtener_interes_mes()) == float

    assert tarjeta.obtener_nueva_deuda() == nueva_deuda
    assert tarjeta.obtener_deuda_recalculada() == deuda_recalculada
    assert tarjeta.obtener_interes_mensual() == tasa / 12
    assert round(tarjeta.obtener_interes_mes(),1) == interes_mes