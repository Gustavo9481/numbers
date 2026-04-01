"""
Tests de integración para el módulo de servicios.
Verifica la comunicación entre Python (services) y el core de Rust.
"""
import pytest
from services.calculator_service import CalculatorService
from schemas.calculation import CalculationResult
from exceptions.calculator import DivisionByZeroError

@pytest.fixture
def calc_service():
    """Fixture que proporciona una instancia limpia del servicio."""
    return CalculatorService()

def test_service_addition(calc_service):
    """Verifica que la suma a través del servicio sea correcta."""
    result = calc_service.perform_addition(10.0, 5.0)
    
    assert isinstance(result, CalculationResult)
    assert result.result == 15.0
    assert result.operation == "suma"
    assert result.inputs == (10.0, 5.0)

def test_service_division_by_zero(calc_service):
    """Verifica que el servicio capture el error de Rust y lance nuestra excepción."""
    with pytest.raises(DivisionByZeroError) as excinfo:
        calc_service.perform_division(10.0, 0.0)
    
    assert "No es posible dividir por cero" in str(excinfo.value)

def test_service_history_management(calc_service):
    """Verifica que el historial registre las operaciones correctamente."""
    # Realizamos un par de operaciones
    calc_service.perform_addition(1.0, 1.0)
    calc_service.perform_multiplication(2.0, 3.0)
    
    history = calc_service.get_history()
    
    assert len(history) == 2
    assert history[0].operation == "suma"
    assert history[1].operation == "multiplicación"
    assert history[1].result == 6.0

def test_service_clear_history(calc_service):
    """Verifica la limpieza del historial."""
    calc_service.perform_addition(5.0, 5.0)
    assert len(calc_service.get_history()) == 1
    
    calc_service.clear_history()
    assert len(calc_service.get_history()) == 0

def test_service_percentage(calc_service):
    """Verifica el cálculo de porcentaje a través del servicio."""
    result = calc_service.perform_percentage(20.0, 200.0)
    
    assert result.result == 40.0
    assert result.operation == "porcentaje"
