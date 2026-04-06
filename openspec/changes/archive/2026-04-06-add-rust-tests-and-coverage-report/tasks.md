## 1. Configuración de Entorno y Cobertura en Python

- [x] 1.1 Añadir `pytest-cov` a las dependencias de desarrollo en `pyproject.toml`
- [x] 1.2 Configurar las opciones de `[tool.pytest.ini_options]` para incluir `--cov=services --cov=schemas --cov-report=term-missing` por defecto
- [x] 1.3 Configurar las opciones de `[tool.coverage.run]` y `[tool.coverage.report]` en `pyproject.toml` para excluir directorios irrelevantes
- [x] 1.4 Ejecutar `uv sync` para instalar la nueva herramienta de cobertura

## 2. Implementación de Tests Nativos en Rust

- [x] 2.1 Añadir bloque de tests unitarios en `core/src/suma.rs` para operaciones multivariable
- [x] 2.2 Añadir bloque de tests unitarios en `core/src/resta.rs`
- [x] 2.3 Añadir bloque de tests unitarios en `core/src/multiplicacion.rs`
- [x] 2.4 Añadir bloque de tests unitarios en `core/src/division.rs` (incluyendo validación de divisor cero)
- [x] 2.5 Añadir bloque de tests unitarios en `core/src/porcentaje.rs`

## 3. Validación y Verificación Final

- [x] 3.1 Ejecutar `cargo test` y verificar que todos los tests nativos de Rust pasen
- [x] 3.2 Ejecutar `uv run pytest` y verificar el reporte de cobertura en terminal
- [x] 3.3 Verificar que la cobertura de `services/` y `schemas/` supere el 80%
