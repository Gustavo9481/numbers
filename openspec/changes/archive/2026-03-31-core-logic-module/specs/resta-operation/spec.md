## ADDED Requirements

### Requirement: Función resta
El sistema SHALL permitir restar dos números de tipo f64 (a - b) y retornar el resultado.

#### Scenario: Resta de enteros positivos
- **WHEN** se llama a resta(5.0, 3.0)
- **THEN** retorna 2.0

#### Scenario: Resta con resultado negativo
- **WHEN** se llama a resta(2.0, 7.0)
- **THEN** retorna -5.0

#### Scenario: Resta de números negativos
- **WHEN** se llama a resta(-5.0, -3.0)
- **THEN** retorna -2.0

#### Scenario: Resta con decimales
- **WHEN** se llama a resta(5.5, 2.3)
- **THEN** retorna 3.2

#### Scenario: Resta con cero
- **WHEN** se llama a resta(5.0, 0.0)
- **THEN** retorna 5.0
