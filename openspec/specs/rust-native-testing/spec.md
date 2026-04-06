## ADDED Requirements

### Requirement: Pruebas unitarias en el núcleo de Rust
El sistema SHALL incluir pruebas unitarias nativas dentro de cada módulo de operación en `core/src/` para validar la lógica matemática sin depender de Python.

#### Scenario: Validación de suma multivariable
- **WHEN** se ejecuta `cargo test` en el directorio `core/`
- **THEN** las pruebas de `suma.rs` deben validar que la suma de `[1.0, 2.0, 3.0]` sea `6.0`

#### Scenario: Validación de división por cero en Rust
- **WHEN** se invoca la función de división con un divisor de `0.0` en los tests de Rust
- **THEN** la prueba debe verificar que se retorne un error o se maneje según la especificación interna

### Requirement: Ejecución independiente de pruebas
El núcleo de Rust MUST permitir la ejecución de sus pruebas de forma independiente de la compilación de la extensión de Python.

#### Scenario: Ejecución de cargo test
- **WHEN** el desarrollador ejecuta `cargo test` desde la raíz o desde `core/`
- **THEN** el sistema debe compilar y ejecutar todos los bloques `#[test]` definidos en los módulos
