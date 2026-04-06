## Why

Asegurar la precisión matemática al nivel más bajo (Rust) y medir sistemáticamente la efectividad de las pruebas mediante reportes de cobertura. Actualmente, la lógica de Rust solo se prueba a través de bindings de Python, lo que dificulta la depuración de errores matemáticos puros y no proporciona visibilidad sobre qué partes del código carecen de pruebas.

## What Changes

- **Tests Nativos en Rust**: Implementación de bloques `#[cfg(test)]` en cada módulo de `core/src/` (`suma.rs`, `resta.rs`, etc.) para validación unitaria.
- **Configuración de Cobertura**: Integración de `pytest-cov` en el entorno de desarrollo.
- **Automatización**: Actualización de `pyproject.toml` con configuraciones predeterminadas para reportes de cobertura (term y html).
- **Documentación de Comandos**: Inclusión de comandos estandarizados para ejecutar tests de Rust y reportes de cobertura en Python.

## Capabilities

### New Capabilities
- `rust-native-testing`: Capacidad de ejecutar pruebas unitarias de bajo nivel directamente en el núcleo de Rust usando `cargo test`.
- `test-coverage-reporting`: Generación automatizada de métricas de cobertura para asegurar que el código de servicios y esquemas cumpla con los estándares de calidad.

### Modified Capabilities
- `multi-value-arithmetic`: Se añadirán requisitos de validación interna a nivel de Rust para las operaciones multivariable.

## Impact

- **Módulos Rust**: `core/src/*.rs` (adición de tests).
- **Configuración Python**: `pyproject.toml` (nuevas dependencias y configuración de herramientas).
- **Workflow**: Cambio en el ciclo de validación para incluir `cargo test` antes de los tests de integración de Python.
