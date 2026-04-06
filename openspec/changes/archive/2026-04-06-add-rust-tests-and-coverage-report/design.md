## Context

El proyecto `numbers` tiene una arquitectura híbrida Rust/Python. Actualmente, la validación se realiza únicamente a través de la capa de Python (`tests/test_core.py` y `tests/test_services.py`). Esto deja una brecha de visibilidad sobre la cobertura del código y la corrección interna de los algoritmos en Rust antes de ser expuestos.

## Goals / Non-Goals

**Goals:**
- Implementar tests unitarios en cada archivo `.rs` de `core/src/`.
- Configurar `pytest-cov` para medir la cobertura de los tests de Python.
- Alcanzar una cobertura mínima del 80% en la capa de servicios y esquemas.
- Centralizar la configuración de herramientas en `pyproject.toml`.

**Non-Goals:**
- Implementar tests de integración complejos en Rust (se delegan a Python).
- Configurar CI/CD (fuera del alcance de esta tarea local).
- Medir la cobertura del código Rust (complejidad técnica innecesaria para este nivel del proyecto).

## Decisions

- **Estructura de Tests en Rust**: Se usará el patrón de "tests internos" mediante `mod tests { ... }` con el atributo `#[cfg(test)]` al final de cada archivo de módulo (`suma.rs`, `resta.rs`, etc.). Esto permite probar funciones privadas si fuera necesario y mantiene la cohesión.
- **Herramienta de Cobertura Python**: `pytest-cov`. Es el estándar para `pytest` y se integra perfectamente con el entorno `uv`.
- **Configuración Centralizada**: Se utilizará el archivo `pyproject.toml` para definir las opciones de `pytest` y `coverage`, evitando archivos `.coveragerc` adicionales.
- **Reporte de Cobertura**: Se generarán reportes en terminal (`term-missing`) y en HTML (`html`) para facilitar la auditoría visual de líneas no cubiertas.

## Risks / Trade-offs

- **[Riesgo] Diversidad de herramientas** → Ejecutar `cargo test` y `pytest` por separado puede ser tedioso.
  - *Mitigación*: Documentar un comando único o usar un `Taskfile`/`Makefile` en el futuro.
- **[Trade-off] Cobertura solo en Python** → No mediremos la cobertura de las líneas de Rust.
  - *Justificación*: La lógica de Rust es pura y matemática; los tests unitarios manuales en Rust son suficientes por ahora sin añadir la sobrecarga de herramientas como `grcov` o `llvm-cov`.
