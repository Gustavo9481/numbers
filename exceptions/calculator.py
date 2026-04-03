"""
Excepciones personalizadas para el servicio de calculadora.
"""

class CalculatorError(Exception):
    """Clase base para errores en el servicio de calculadora."""
    pass

class DivisionByZeroError(CalculatorError):
    """Error lanzado cuando se intenta dividir por cero."""
    pass

class InvalidOperationError(CalculatorError):
    """Error lanzado cuando se solicita una operación no válida."""
    pass

class CalculationOverflowError(CalculatorError):
    """Error lanzado cuando el resultado excede los límites numéricos."""
    pass

# NOTE: notas realizadas
