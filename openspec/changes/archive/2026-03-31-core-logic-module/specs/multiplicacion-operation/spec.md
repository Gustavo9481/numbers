## ADDED Requirements

### Requirement: Función multiplicación
El sistema SHALL permitir multiplicar dos números de tipo f64 y retornar el resultado.

#### Scenario: Multiplicación de enteros positivos
- **WHEN** se llama a multiplicacion(4.0, 3.0)
- **THEN** retorna 12.0

#### Scenario: Multiplicación con resultado negativo
- **WHEN** se llama a multiplicacion(-4.0, 3.0)
- **THEN** retorna -12.0

#### Scenario: Multiplicación de números negativos
- **WHEN** se llama a multiplicacion(-4.0, -3.0)
- **THEN** retorna 12.0

#### Scenario: Multiplicación con decimales
- **WHEN** se llama a multiplicacion(2.5, 4.0)
- **THEN** retorna 10.0

#### Scenario: Multiplicación con cero
- **WHEN** se llama a multiplicacion(5.0, 0.0)
- **THEN** retorna 0.0
