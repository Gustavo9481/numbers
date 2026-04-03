## Why

Las operaciones actuales de la calculadora están limitadas a dos operandos (A y B), lo cual restringe la versatilidad de la herramienta. Una calculadora profesional debe ser capaz de procesar series de datos de forma eficiente (ej: sumar una lista de 10 números en una sola llamada) para mejorar el rendimiento y la experiencia de usuario en la interfaz final.

## What Changes

- **BREAKING**: El núcleo de Rust (`pycalc_core`) se rediseña para aceptar vectores de números (`Vec<f64>`) en todas sus operaciones aritméticas fundamentales.
- **BREAKING**: La interfaz del motor (`ICalculatorEngine`) y el servicio (`CalculatorService`) en Python se actualizan para manejar colecciones de valores.
- **Mejora de API**: El servicio de Python implementará argumentos variables (`*args`) para permitir una interacción natural (ej: `add(1, 2, 3)`).
- **Consistencia**: Se estandariza el comportamiento de la resta y división sobre múltiples valores (operación secuencial).

## Capabilities

### New Capabilities
- `multi-value-arithmetic`: Capacidad de realizar operaciones de suma, resta, multiplicación y división sobre una secuencia indeterminada de valores numéricos.

### Modified Capabilities
- (Ninguna existente que requiera modificación de requerimientos base)

## Impact

- **Core (Rust)**: `core/src/suma.rs`, `core/src/resta.rs`, `core/src/multiplicacion.rs`, `core/src/division.rs`.
- **Servicios (Python)**: `services/calculator_service.py` y el protocolo `ICalculatorEngine`.
- **Validación**: `tests/test_core.py` y `tests/test_services.py` requieren una actualización completa para validar los nuevos casos de uso multivariable.
