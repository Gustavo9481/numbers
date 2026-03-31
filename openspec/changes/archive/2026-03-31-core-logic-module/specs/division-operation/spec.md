## ADDED Requirements

### Requirement: Función división
El sistema SHALL permitir dividir dos números de tipo f64 (a / b) y retornar el resultado. Cuando b es 0.0, SHALL retornar un error de división por cero.

#### Scenario: División de enteros positivos
- **WHEN** se llama a division(10.0, 2.0)
- **THEN** retorna 5.0

#### Scenario: División con resultado decimal
- **WHEN** se llama a division(7.0, 2.0)
- **THEN** retorna 3.5

#### Scenario: División con números negativos
- **WHEN** se llama a division(-10.0, 2.0)
- **THEN** retorna -5.0

#### Scenario: División por cero
- **WHEN** se llama a division(5.0, 0.0)
- **THEN** retorna error "DivisionByZero"

#### Scenario: División con cero como numerador
- **WHEN** se llama a division(0.0, 5.0)
- **THEN** retorna 0.0
