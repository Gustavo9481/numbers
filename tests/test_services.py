"""
Pruebas de integración para la capa de servicios de la calculadora.
"""
import pytest
from services.calculator_service import CalculatorService
from exceptions.calculator import DivisionByZeroError
from schemas.calculation import CalculationResult

@pytest.fixture
def service():
    """Retorna una instancia fresca del servicio de calculadora."""
    return CalculatorService()

class TestServiceArithmetic:
    """Verifica que el servicio maneja correctamente las operaciones multivariable."""

    def test_perform_addition_multi(self, service):
        """Prueba la suma con múltiples argumentos variables."""
        res = service.perform_addition(1, 2, 3, 4)
        assert res.result == 10.0
        assert res.operation == "suma"
        assert res.inputs == (1, 2, 3, 4)

    def test_perform_subtraction_multi(self, service):
        """Prueba la resta con múltiples argumentos variables."""
        res = service.perform_subtraction(100, 20, 10)
        assert res.result == 70.0
        assert res.inputs == (100, 20, 10)

    def test_perform_multiplication_multi(self, service):
        """Prueba la multiplicación con múltiples argumentos variables."""
        res = service.perform_multiplication(2, 3, 4)
        assert res.result == 24.0

    def test_perform_division_multi(self, service):
        """Prueba la división con múltiples argumentos variables."""
        res = service.perform_division(100, 2, 5)
        assert res.result == 10.0

    def test_perform_division_by_zero(self, service):
        """Prueba el manejo de errores en división por cero."""
        with pytest.raises(DivisionByZeroError):
            service.perform_division(10, 0, 5)

    def test_perform_percentage(self, service):
        """Prueba el cálculo de porcentaje (sigue siendo binario)."""
        res = service.perform_percentage(50, 200)
        assert res.result == 100.0

class TestServiceHistory:
    """Verifica la gestión del historial en el servicio."""

    def test_history_recording(self, service):
        """Asegura que los cálculos se graban en el historial."""
        service.perform_addition(1, 1)
        service.perform_multiplication(2, 2)
        
        history = service.get_history()
        assert len(history) == 2
        assert history[0].operation == "suma"
        assert history[1].operation == "multiplicación"

    def test_clear_history(self, service):
        """Prueba el vaciado del historial."""
        service.perform_addition(1, 1)
        service.clear_history()
        assert len(service.get_history()) == 0
