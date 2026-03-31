## 1. Configuración del Proyecto

- [x] 1.1 Verificar que existe pyproject.toml en la raíz
- [x] 1.2 Crear estructura core/src/ si no existe
- [x] 1.3 Crear archivo Cargo.toml en core/ con dependencias pyo3 y thiserror

## 2. Implementación de Funciones Rust

- [x] 2.1 Crear archivo core/src/suma.rs con función add
- [x] 2.2 Crear archivo core/src/resta.rs con función subtract
- [x] 2.3 Crear archivo core/src/multiplicacion.rs con función multiply
- [x] 2.4 Crear archivo core/src/division.rs con función divide (manejo de división por cero)
- [x] 2.5 Crear archivo core/src/porcentaje.rs con función percentage
- [x] 2.6 Crear archivo core/src/lib.rs que importe y exporte todas las funciones

## 3. Exposición a Python (PyO3)

- [x] 3.1 Agregar macros #[pyfunction] a cada función
- [x] 3.2 Registrar funciones en el módulo PyO3
- [x] 3.3 Compilar módulo con maturin develop

## 4. Testing

- [x] 4.1 Crear archivo tests/test_core.py
- [x] 4.2 Escribir tests para suma (enteros, decimales, negativos, cero)
- [x] 4.3 Escribir tests para resta (enteros, decimales, negativos, cero)
- [x] 4.4 Escribir tests para multiplicacion (enteros, decimales, negativos, cero)
- [x] 4.5 Escribir tests para division (enteros, decimales, división por cero)
- [x] 4.6 Escribir tests para porcentaje (casos básicos, borde)
- [x] 4.7 Ejecutar pytest y verificar cobertura >80%

## 5. Verificación

- [x] 5.1 Ejecutar cargo clippy sin warnings
- [x] 5.2 Ejecutar cargo fmt
- [x] 5.3 Verificar que todas las funciones se importan correctamente desde Python
