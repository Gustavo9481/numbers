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
    """Define la interfaz para el motor de cálculo subyacente."""
    def sumar(self, numbers: List[float]) -> float: ...
    def subtract(self, numbers: List[float]) -> float: ...
    def multiply(self, numbers: List[float]) -> float: ...
    def divide(self, numbers: List[float]) -> float: ...
    def percentage(self, value: float, total: float) -> float: ...

class CalculatorService:
    """Servicio que coordina la ejecución de operaciones matemáticas."""

    def __init__(self, engine: Any = pycalc_core):
        self._engine = engine
        self._history: List[CalculationResult] = []

    def perform_addition(self, *args: float) -> CalculationResult:
        """Realiza una suma de múltiples valores."""
        numbers = list(args)
        res = self._engine.sumar(numbers)
        return self._record_calculation("suma", res, args)

    def perform_subtraction(self, *args: float) -> CalculationResult:
        """Realiza una resta secuencial de múltiples valores."""
        numbers = list(args)
        res = self._engine.subtract(numbers)
        return self._record_calculation("resta", res, args)

    def perform_multiplication(self, *args: float) -> CalculationResult:
        """Realiza una multiplicación de múltiples valores."""
        numbers = list(args)
        res = self._engine.multiply(numbers)
        return self._record_calculation("multiplicación", res, args)

    def perform_division(self, *args: float) -> CalculationResult:
        """Realiza una división secuencial con manejo seguro de errores."""
        numbers = list(args)
        try:
            res = self._engine.divide(numbers)
            return self._record_calculation("división", res, args)
        except ZeroDivisionError:
            raise DivisionByZeroError("No es posible dividir por cero desde el motor de cálculo.")

    def perform_percentage(self, value: float, total: float) -> CalculationResult:
        """Realiza un cálculo de porcentaje."""
        res = self._engine.percentage(value, total)
        return self._record_calculation("porcentaje", res, (value, total))

    def _record_calculation(self, op: str, result: float, inputs: tuple) -> CalculationResult:
        calc_res = CalculationResult(operation=op, result=result, inputs=inputs)
        self._history.append(calc_res)
        return calc_res

    def get_history(self, limit: int = 10) -> List[CalculationResult]:
        return self._history[-limit:]

    def clear_history(self) -> None:
        self._history.clear()
