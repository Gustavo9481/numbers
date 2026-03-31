import pytest
import pycalc_core


class TestSuma:
    def test_suma_enteros_positivos(self):
        assert pycalc_core.add(2.0, 3.0) == 5.0

    def test_suma_numeros_negativos(self):
        assert pycalc_core.add(-5.0, -3.0) == -8.0

    def test_suma_positivo_y_negativo(self):
        assert pycalc_core.add(10.0, -4.0) == 6.0

    def test_suma_con_decimales(self):
        assert pycalc_core.add(1.5, 2.5) == 4.0

    def test_suma_con_cero(self):
        assert pycalc_core.add(5.0, 0.0) == 5.0


class TestResta:
    def test_resta_enteros_positivos(self):
        assert pycalc_core.subtract(5.0, 3.0) == 2.0

    def test_resta_resultado_negativo(self):
        assert pycalc_core.subtract(2.0, 7.0) == -5.0

    def test_resta_numeros_negativos(self):
        assert pycalc_core.subtract(-5.0, -3.0) == -2.0

    def test_resta_con_decimales(self):
        assert pycalc_core.subtract(5.5, 2.3) == pytest.approx(3.2)

    def test_resta_con_cero(self):
        assert pycalc_core.subtract(5.0, 0.0) == 5.0


class TestMultiplicacion:
    def test_multiplicacion_enteros_positivos(self):
        assert pycalc_core.multiply(4.0, 3.0) == 12.0

    def test_multiplicacion_resultado_negativo(self):
        assert pycalc_core.multiply(-4.0, 3.0) == -12.0

    def test_multiplicacion_numeros_negativos(self):
        assert pycalc_core.multiply(-4.0, -3.0) == 12.0

    def test_multiplicacion_con_decimales(self):
        assert pycalc_core.multiply(2.5, 4.0) == 10.0

    def test_multiplicacion_con_cero(self):
        assert pycalc_core.multiply(5.0, 0.0) == 0.0


class TestDivision:
    def test_division_enteros_positivos(self):
        assert pycalc_core.divide(10.0, 2.0) == 5.0

    def test_division_resultado_decimal(self):
        assert pycalc_core.divide(7.0, 2.0) == 3.5

    def test_division_numeros_negativos(self):
        assert pycalc_core.divide(-10.0, 2.0) == -5.0

    def test_division_por_cero(self):
        with pytest.raises(ZeroDivisionError):
            pycalc_core.divide(5.0, 0.0)

    def test_division_cero_como_numerador(self):
        assert pycalc_core.divide(0.0, 5.0) == 0.0


class TestPorcentaje:
    def test_porcentaje_basico(self):
        assert pycalc_core.percentage(50.0, 100.0) == 50.0

    def test_porcentaje_menor_al_total(self):
        assert pycalc_core.percentage(25.0, 200.0) == 50.0

    def test_porcentaje_mayor_al_total(self):
        assert pycalc_core.percentage(150.0, 100.0) == 150.0

    def test_porcentaje_con_decimales(self):
        assert pycalc_core.percentage(33.33, 100.0) == pytest.approx(33.33)

    def test_porcentaje_cero_como_valor(self):
        assert pycalc_core.percentage(0.0, 100.0) == 0.0

    def test_porcentaje_cero_como_total(self):
        assert pycalc_core.percentage(50.0, 0.0) == 0.0
