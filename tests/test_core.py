"""Pruebas unitarias para el núcleo de la calculadora (pycalc_core)."""

import pytest
import pycalc_core


class TestSuma:
    """Conjunto de pruebas para la operación de suma multivariable."""

    def test_suma_lista_positivos(self):
        """Prueba la suma de una lista de números positivos."""
        assert pycalc_core.sumar([2.0, 3.0, 5.0]) == 10.0

    def test_suma_lista_con_negativos(self):
        """Prueba la suma con números negativos."""
        assert pycalc_core.sumar([-5.0, 10.0, -3.0]) == 2.0

    def test_suma_lista_vacia(self):
        """Prueba que la suma de una lista vacía es 0.0."""
        assert pycalc_core.sumar([]) == 0.0


class TestResta:
    """Conjunto de pruebas para la operación de resta secuencial."""

    def test_resta_secuencial(self):
        """Prueba la resta de múltiples valores."""
        assert pycalc_core.subtract([100.0, 20.0, 10.0]) == 70.0

    def test_resta_unico_elemento(self):
        """Prueba que la resta de un solo elemento retorna el mismo elemento."""
        assert pycalc_core.subtract([50.0]) == 50.0

    def test_resta_lista_vacia(self):
        """Prueba que la resta de una lista vacía es 0.0."""
        assert pycalc_core.subtract([]) == 0.0


class TestMultiplicacion:
    """Conjunto de pruebas para la operación de multiplicación multivariable."""

    def test_multiplicacion_lista(self):
        """Prueba el producto de varios números."""
        assert pycalc_core.multiply([2.0, 3.0, 4.0]) == 24.0

    def test_multiplicacion_con_cero(self):
        """Prueba que cualquier producto con cero es cero."""
        assert pycalc_core.multiply([10.0, 0.0, 5.0]) == 0.0

    def test_multiplicacion_lista_vacia(self):
        """Prueba que la multiplicación de una lista vacía retorna 0.0."""
        assert pycalc_core.multiply([]) == 0.0


class TestDivision:
    """Conjunto de pruebas para la operación de división secuencial."""

    def test_division_secuencial(self):
        """Prueba la división de múltiples valores."""
        assert pycalc_core.divide([100.0, 2.0, 5.0]) == 10.0

    def test_division_por_cero_en_secuencia(self):
        """Prueba que la división por cero lanza ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            pycalc_core.divide([100.0, 5.0, 0.0, 2.0])

    def test_division_lista_vacia(self):
        """Prueba que la división de una lista vacía es 0.0."""
        assert pycalc_core.divide([]) == 0.0


class TestPorcentaje:
    """Conjunto de pruebas para el cálculo de porcentajes."""

    def test_porcentaje_basico(self):
        assert pycalc_core.percentage(50.0, 100.0) == 50.0

    def test_porcentaje_cero_como_total(self):
        assert pycalc_core.percentage(50.0, 0.0) == 0.0
