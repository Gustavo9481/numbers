## 1. Refactorización del Core en Rust

- [x] 1.1 Actualizar `core/src/suma.rs` para aceptar `Vec<f64>` y usar el iterador `sum()`.
- [x] 1.2 Actualizar `core/src/resta.rs` para implementar resta secuencial sobre `Vec<f64>`.
- [x] 1.3 Actualizar `core/src/multiplicacion.rs` para aceptar `Vec<f64>` y usar el iterador `product()`.
- [x] 1.4 Actualizar `core/src/division.rs` para implementar división secuencial con validación de ceros sobre `Vec<f64>`.
- [x] 1.5 Modificar `core/src/lib.rs` para actualizar las firmas de las funciones expuestas a PyO3.

## 2. Adaptación de la Capa de Servicios (Python)

- [x] 2.1 Actualizar el protocolo `ICalculatorEngine` en `services/calculator_service.py` para reflejar las firmas de `Vec<f64>`.
- [x] 2.2 Refactorizar `CalculatorService` para usar argumentos variables (`*args`) en todos los métodos de operación.
- [x] 2.3 Asegurar que `schemas/calculation.py` maneje correctamente los inputs de longitud variable en el historial.

## 3. Validación y Pruebas

- [x] 3.1 Actualizar `tests/test_core.py` con casos de prueba para múltiples valores y listas vacías.
- [x] 3.2 Actualizar `tests/test_services.py` para verificar la ergonomía de la API con `*args`.
- [x] 3.3 Compilar el core con `maturin develop` y ejecutar la suite completa de `pytest`.
