"""
Modelos de datos para el servicio de calculadora.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass(frozen=True)
class CalculationResult:
    """Representa el resultado de una operación matemática.
    
    Attributes:
        operation (str): El nombre de la operación realizada.
        result (float): El valor numérico resultante.
        timestamp (datetime): La fecha y hora en que se realizó el cálculo.
        inputs (tuple[float, ...]): Los valores de entrada utilizados.
        metadata (dict): Información adicional sobre la ejecución.
    """
    operation: str
    result: float
    inputs: tuple[float, ...]
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: dict = field(default_factory=dict)

    def __str__(self) -> str:
        """Representación legible del resultado."""
        return f"{self.operation.capitalize()}: {self.result} (Calculado el {self.timestamp.strftime('%H:%M:%S')})"
