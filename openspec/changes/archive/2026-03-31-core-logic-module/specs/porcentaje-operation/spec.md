## ADDED Requirements

### Requirement: Función porcentaje
El sistema SHALL permitir calcular el porcentaje de un valor respecto a un total (a * b / 100) y retornar el resultado.

#### Scenario: Porcentaje básico
- **WHEN** se llama a porcentaje(50.0, 100.0)
- **THEN** retorna 50.0

#### Scenario: Porcentaje menor al total
- **WHEN** se llama a porcentaje(25.0, 200.0)
- **THEN** retorna 50.0

#### Scenario: Porcentaje mayor al total
- **WHEN** se llama a porcentaje(150.0, 100.0)
- **THEN** retorna 150.0

#### Scenario: Porcentaje con decimales
- **WHEN** se llama a porcentaje(33.33, 100.0)
- **THEN** retorna 33.33

#### Scenario: Porcentaje con cero como valor
- **WHEN** se llama a porcentaje(0.0, 100.0)
- **THEN** retorna 0.0

#### Scenario: Porcentaje con cero como total
- **WHEN** se llama a porcentaje(50.0, 0.0)
- **THEN** retorna 0.0
