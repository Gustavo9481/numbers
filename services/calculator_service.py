"""
Módulo de servicio para la calculadora.
Proporciona una interfaz profesional para el motor de cálculo en Rust (pycalc_core).
"""
import pycalc_core
from datetime import datetime
from typing import Any, List, Protocol, runtime_checkable

from exceptions.calculator import DivisionByZeroError, InvalidOperationError
from schemas.calculation import CalculationResult

@runtime_checkable
class ICalculatorEngine(Protocol):
    """Define la interfaz para el motor de cálculo subyacente.
    
    Este protocolo permite cambiar el motor de Rust por uno de Python puro o un Mock
    sin necesidad de modificar el servicio de calculadora.
    """
    def add(self, a: float, b: float) -> float: ...
    def subtract(self, a: float, b: float) -> float: ...
    def multiply(self, a: float, b: float) -> float: ...
    def divide(self, a: float, b: float) -> float: ...
    def percentage(self, value: float, total: float) -> float: ...

class CalculatorService:
    """Servicio que coordina la ejecución de operaciones matemáticas.
    
    Actúa como capa de abstracción sobre el motor de cálculo (Rust core), 
    proporcionando validación, gestión de errores y formateo de resultados.
    """

    def __init__(self, engine: Any = pycalc_core):
        """Inicializa el servicio con un motor de cálculo.
        
        Args:
            engine: El motor de cálculo subyacente. Por defecto usa pycalc_core (Rust).
        """
        self._engine = engine
        self._history: List[CalculationResult] = []

    def perform_addition(self, a: float, b: float) -> CalculationResult:
        """Realiza una suma y retorna un objeto CalculationResult."""
        res = self._engine.add(a, b)
        return self._record_calculation("suma", res, (a, b))

    def perform_subtraction(self, a: float, b: float) -> CalculationResult:
        """Realiza una resta y retorna un objeto CalculationResult."""
        res = self._engine.subtract(a, b)
        return self._record_calculation("resta", res, (a, b))

    def perform_multiplication(self, a: float, b: float) -> CalculationResult:
        """Realiza una multiplicación y retorna un objeto CalculationResult."""
        res = self._engine.multiply(a, b)
        return self._record_calculation("multiplicación", res, (a, b))

    def perform_division(self, a: float, b: float) -> CalculationResult:
        """Realiza una división con manejo seguro de errores."""
        try:
            res = self._engine.divide(a, b)
            return self._record_calculation("división", res, (a, b))
        except ZeroDivisionError:
            raise DivisionByZeroError("No es posible dividir por cero desde el motor de cálculo.")

    def perform_percentage(self, value: float, total: float) -> CalculationResult:
        """Realiza un cálculo de porcentaje."""
        res = self._engine.percentage(value, total)
        return self._record_calculation("porcentaje", res, (value, total))

    def _record_calculation(self, op: str, result: float, inputs: tuple) -> CalculationResult:
        """Registra internamente el cálculo y lo retorna como un esquema."""
        calc_res = CalculationResult(operation=op, result=result, inputs=inputs)
        self._history.append(calc_res)
        return calc_res

    def get_history(self, limit: int = 10) -> List[CalculationResult]:
        """Retorna los últimos cálculos realizados."""
        return self._history[-limit:]

    def clear_history(self) -> None:
        """Limpia el historial de cálculos."""
        self._history.clear()
