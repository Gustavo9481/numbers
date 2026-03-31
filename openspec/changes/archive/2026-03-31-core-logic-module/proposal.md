## Why

El proyecto PyCalc requiere un módulo de lógica core en Rust que exponga operaciones matemáticas básicas a Python via PyO3. Este módulo es la base para toda la funcionalidad de la calculadora y debe ser implementado primero antes de construir las capas de servicios y UI.

## What Changes

- Crear módulo Rust con funciones para operaciones matemáticas básicas
- Implementar 5 operaciones: suma, resta, multiplicación, división, porcentaje
- Exponer funciones a Python usando PyO3
- Crear tests unitarios con pytest cubriendo múltiples casos de prueba

## Capabilities

### New Capabilities

- `suma-operation`: Función para sumar dos números float
- `resta-operation`: Función para restar dos números float
- `multiplicacion-operation`: Función para multiplicar dos números float
- `division-operation`: Función para dividir dos números float con manejo de división por cero
- `porcentaje-operation`: Función para calcular porcentaje entre dos números

## Impact

- Nuevo módulo `core/` en Rust
- Archivo `core/src/lib.rs` con funciones expuestas
- Tests en `tests/test_core.py` para cada operación
- Dependencias: pyo3, thiserror en Cargo.toml
