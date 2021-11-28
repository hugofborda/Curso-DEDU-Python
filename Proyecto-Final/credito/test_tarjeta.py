from credito.tarjeta import Tarjeta
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
    assert tarjeta.obtener_nueva_deuda() == nueva_deuda
    assert tarjeta.obtener_deuda_recalculada() == deuda_recalculada