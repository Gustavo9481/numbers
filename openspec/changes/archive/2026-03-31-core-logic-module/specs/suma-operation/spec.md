## ADDED Requirements

### Requirement: Función suma
El sistema SHALL permitir sumar dos números de tipo f64 y retornar el resultado.

#### Scenario: Suma de enteros positivos
- **WHEN** se llama a suma(2.0, 3.0)
- **THEN** retorna 5.0

#### Scenario: Suma de números negativos
- **WHEN** se llama a suma(-5.0, -3.0)
- **THEN** retorna -8.0

#### Scenario: Suma de positivo y negativo
- **WHEN** se llama a suma(10.0, -4.0)
- **THEN** retorna 6.0

#### Scenario: Suma con decimales
- **WHEN** se llama a suma(1.5, 2.5)
- **THEN** retorna 4.0

#### Scenario: Suma con cero
- **WHEN** se llama a suma(5.0, 0.0)
- **THEN** retorna 5.0
