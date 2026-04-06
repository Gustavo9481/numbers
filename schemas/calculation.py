"""
Modelos de datos para el servicio de calculadora utilizando Pydantic.
"""
from datetime import datetime
from typing import Dict, Tuple

from pydantic import BaseModel, ConfigDict, Field


class CalculationResult(BaseModel):
    """Representa el resultado de una operación matemática.

    Attributes:
        operation (str): El nombre de la operación realizada.
        result (float): El valor numérico resultante.
        timestamp (datetime): La fecha y hora en que se realizó el cálculo.
        inputs (Tuple[float, ...]): Los valores de entrada utilizados.
        metadata (Dict): Información adicional sobre la ejecución.
    """

    model_config = ConfigDict(frozen=True)

    operation: str
    result: float
    inputs: Tuple[float, ...]
    timestamp: datetime = Field(default_factory=datetime.now)
    metadata: Dict = Field(default_factory=dict)

    def __str__(self) -> str:
        """Representación legible del resultado."""
        return (
            f"{self.operation.capitalize()}: {self.result} "
            f"(Calculado el {self.timestamp.strftime('%H:%M:%S')})"
        )
