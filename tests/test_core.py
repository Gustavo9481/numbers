"""Pruebas unitarias para el núcleo de la calculadora (pycalc_core).

Este módulo contiene las pruebas de integración para las funciones matemáticas
implementadas en Rust y expuestas a Python.
"""

import pytest
import pycalc_core


class TestSuma:
    """Conjunto de pruebas para la operación de suma."""

    def test_suma_enteros_positivos(self):
        """Prueba la suma de dos números flotantes positivos."""
        assert pycalc_core.add(2.0, 3.0) == 5.0

    def test_suma_numeros_negativos(self):
        """Prueba la suma de dos números flotantes negativos."""
        assert pycalc_core.add(-5.0, -3.0) == -8.0

    def test_suma_positivo_y_negativo(self):
        """Prueba la suma de un número positivo y uno negativo."""
        assert pycalc_core.add(10.0, -4.0) == 6.0

    def test_suma_con_decimales(self):
        """Prueba la suma de números con parte decimal."""
        assert pycalc_core.add(1.5, 2.5) == 4.0

    def test_suma_con_cero(self):
        """Prueba la suma de un número con cero."""
        assert pycalc_core.add(5.0, 0.0) == 5.0


class TestResta:
    """Conjunto de pruebas para la operación de resta."""

    def test_resta_enteros_positivos(self):
        """Prueba la resta de dos números flotantes positivos."""
        assert pycalc_core.subtract(5.0, 3.0) == 2.0

    def test_resta_resultado_negativo(self):
        """Prueba que la resta puede resultar en un valor negativo."""
        assert pycalc_core.subtract(2.0, 7.0) == -5.0

    def test_resta_numeros_negativos(self):
        """Prueba la resta de dos números negativos."""
        assert pycalc_core.subtract(-5.0, -3.0) == -2.0

    def test_resta_con_decimales(self):
        """Prueba la resta con números decimales usando precisión aproximada."""
        assert pycalc_core.subtract(5.5, 2.3) == pytest.approx(3.2)

    def test_resta_con_cero(self):
        """Prueba la resta de un número con cero."""
        assert pycalc_core.subtract(5.0, 0.0) == 5.0


class TestMultiplicacion:
    """Conjunto de pruebas para la operación de multiplicación."""

    def test_multiplicacion_enteros_positivos(self):
        """Prueba la multiplicación de dos números positivos."""
        assert pycalc_core.multiply(4.0, 3.0) == 12.0

    def test_multiplicacion_resultado_negativo(self):
        """Prueba la multiplicación que resulta en un valor negativo."""
        assert pycalc_core.multiply(-4.0, 3.0) == -12.0

    def test_multiplicacion_numeros_negativos(self):
        """Prueba la multiplicación de dos números negativos."""
        assert pycalc_core.multiply(-4.0, -3.0) == 12.0

    def test_multiplicacion_con_decimales(self):
        """Prueba la multiplicación con números decimales."""
        assert pycalc_core.multiply(2.5, 4.0) == 10.0

    def test_multiplicacion_con_cero(self):
        """Prueba que cualquier número multiplicado por cero es cero."""
        assert pycalc_core.multiply(5.0, 0.0) == 0.0


class TestDivision:
    """Conjunto de pruebas para la operación de división."""

    def test_division_enteros_positivos(self):
        """Prueba la división exacta entre dos números flotantes."""
        assert pycalc_core.divide(10.0, 2.0) == 5.0

    def test_division_resultado_decimal(self):
        """Prueba la división con resultado decimal."""
        assert pycalc_core.divide(7.0, 2.0) == 3.5

    def test_division_numeros_negativos(self):
        """Prueba la división que involucra números negativos."""
        assert pycalc_core.divide(-10.0, 2.0) == -5.0

    def test_division_por_cero(self):
        """Prueba que la división por cero lanza ZeroDivisionError desde Rust."""
        with pytest.raises(ZeroDivisionError):
            pycalc_core.divide(5.0, 0.0)

    def test_division_cero_como_numerador(self):
        """Prueba que el cero dividido por cualquier número es cero."""
        assert pycalc_core.divide(0.0, 5.0) == 0.0


class TestPorcentaje:
    """Conjunto de pruebas para el cálculo de porcentajes."""

    def test_porcentaje_basico(self):
        """Prueba el cálculo de porcentaje estándar."""
        assert pycalc_core.percentage(50.0, 100.0) == 50.0

    def test_porcentaje_menor_al_total(self):
        """Prueba un porcentaje menor al total."""
        assert pycalc_core.percentage(25.0, 200.0) == 50.0

    def test_porcentaje_mayor_al_total(self):
        """Prueba un porcentaje que excede el 100%."""
        assert pycalc_core.percentage(150.0, 100.0) == 150.0

    def test_porcentaje_con_decimales(self):
        """Prueba el cálculo de porcentaje con precisión aproximada."""
        assert pycalc_core.percentage(33.33, 100.0) == pytest.approx(33.33)

    def test_porcentaje_cero_como_valor(self):
        """Prueba que el 0% de cualquier valor es cero."""
        assert pycalc_core.percentage(0.0, 100.0) == 0.0

    def test_porcentaje_cero_como_total(self):
        """Prueba el porcentaje sobre un total de cero."""
        assert pycalc_core.percentage(50.0, 0.0) == 0.0
