# project.md
<!-- OpenSpec v1.0 — Machine-readable project specification -->

```yaml
openspec: "1.0"
project:
  name: PyCalc
  version: 0.1.0
  description: >
    Calculadora multiplataforma con lógica de negocio en Rust expuesta a Python
    via PyO3, interfaz nativa multiplataforma construida con Flet (Flutter engine).
  license: MIT
  language: python
  python_version: ">=3.12"
```

---

## Metadatos

| Campo | Valor |
|---|---|
| **Proyecto** | PyCalc |
| **Versión** | 0.1.0 |
| **Tipo** | Desktop / Mobile App |
| **Plataformas** | Windows · macOS · Linux · iOS · Android |
| **Última actualización** | 2026-03-26 |

---

## Objetivo

Calculadora con arquitectura modular que separa responsabilidades en capas bien definidas. El objetivo secundario es servir como proyecto de referencia para integración Rust↔Python via PyO3 con interfaz Flet.

---

## Stack

```yaml
stack:
  core:
    language: rust
    version: ">=1.78"
    bridge: pyo3
    pyo3_version: ">=0.21"
    build_tool: maturin
    maturin_version: ">=1.5"

  application:
    language: python
    version: ">=3.12"
    dependency_manager: uv
    uv_version: ">=0.4"

  ui:
    framework: flet
    flet_version: ">=0.24"
    render_engine: flutter
    targets:
      - desktop
      - mobile
      - web

  testing:
    framework: pytest
    pytest_version: ">=8.0"
    coverage: pytest-cov
    minimum_coverage: 80

  linting:
    python: ruff
    rust: clippy
    format_python: ruff format
    format_rust: rustfmt
```

---

## Arquitectura

```yaml
architecture:
  pattern: layered
  layers:
    - name: core
      language: rust
      path: core/src/lib.rs
      responsibility: >
        Lógica matemática pura. Operaciones aritméticas, validación de
        expresiones, manejo de historial en memoria, errores matemáticos.
      exposes_to: python via PyO3 #[pyfunction] macros
      dependencies: []

    - name: services
      language: python
      path: pycalc/services/
      responsibility: >
        Orquestación. Conecta la UI con el módulo Rust. Formatea resultados,
        maneja el estado de la sesión de cálculo.
      exposes_to: ui layer
      dependencies:
        - core (Rust module compiled via maturin)

    - name: ui
      language: python
      path: pycalc/ui/
      framework: flet
      responsibility: >
        Renderizado de la interfaz, captura de eventos del usuario,
        presentación de resultados y errores.
      exposes_to: end user
      dependencies:
        - services layer
        - theme.py
```

---

## Estructura de Archivos

```yaml
file_structure:
  root:
    - AGENTS.md
    - project.md
    - pyproject.toml
    - Cargo.toml

  core/:
    - Cargo.toml
    - src/lib.rs

  pycalc/:
    - __init__.py
    - services/:
        - __init__.py
        - calculator.py
    - ui/:
        - __init__.py
        - app.py
        - theme.py
        - components/:
            - __init__.py
            - display.py
            - keypad.py

  tests/:
    - __init__.py
    - test_core.py
    - test_services.py
```

---

## Módulo Core (Rust)

```yaml
core_module:
  name: pycalc_core
  type: native python extension (.pyd / .so)

  operations:
    - id: add
      signature: "add(a: f64, b: f64) -> PyResult<f64>"
      description: Suma dos números de punto flotante

    - id: subtract
      signature: "subtract(a: f64, b: f64) -> PyResult<f64>"
      description: Resta b de a

    - id: multiply
      signature: "multiply(a: f64, b: f64) -> PyResult<f64>"
      description: Multiplica dos números

    - id: divide
      signature: "divide(a: f64, b: f64) -> PyResult<f64>"
      description: Divide a entre b. Error si b == 0.0

    - id: modulo
      signature: "modulo(a: f64, b: f64) -> PyResult<f64>"
      description: Residuo de la división. Error si b == 0.0

    - id: power
      signature: "power(base: f64, exp: f64) -> PyResult<f64>"
      description: Potenciación base^exp

    - id: sqrt
      signature: "sqrt(n: f64) -> PyResult<f64>"
      description: Raíz cuadrada. Error si n < 0.0

  error_types:
    - DivisionByZero
    - NegativeSqrt
    - Overflow
    - InvalidInput

  history:
    description: >
      Estructura en memoria que almacena las últimas N operaciones realizadas
      en la sesión actual. Se reinicia al cerrar la app.
    max_entries: 50
```

---

## Interfaces Python

```yaml
services:
  CalculatorService:
    path: pycalc/services/calculator.py
    description: >
      Clase principal de orquestación. Instancia el módulo Rust, 
      delega cálculos y formatea respuestas para la UI.
    
    public_methods:
      - name: calculate
        signature: "calculate(expression: str) -> CalculationResult"
        description: Parsea una expresión y delega al módulo Rust

      - name: get_history
        signature: "get_history() -> list[HistoryEntry]"
        description: Retorna el historial de la sesión

      - name: clear
        signature: "clear() -> None"
        description: Limpia el estado actual del display

    types:
      CalculationResult:
        fields:
          - value: float | None
          - error: str | None
          - expression: str

      HistoryEntry:
        fields:
          - expression: str
          - result: float
          - timestamp: datetime

ui:
  entry_point: pycalc/ui/app.py
  
  components:
    - name: Display
      path: pycalc/ui/components/display.py
      props:
        - expression: str
        - result: str
        - error: str | None

    - name: Keypad
      path: pycalc/ui/components/keypad.py
      props:
        - on_press: Callable[[str], None]

  theme:
    path: pycalc/ui/theme.py
    exports:
      - COLORS
      - TYPOGRAPHY
      - SPACING
```

---

## Dependencias

```yaml
dependencies:
  python:
    runtime:
      - flet>=0.24
    build:
      - maturin>=1.5
    dev:
      - pytest>=8.0
      - pytest-cov>=5.0
      - ruff>=0.4

  rust:
    runtime:
      - pyo3 = { version = "0.21", features = ["extension-module"] }
      - thiserror = "1.0"
    dev:
      - (testing nativo de cargo)
```

---

## Comandos de Desarrollo

```yaml
commands:
  setup:
    - cmd: uv sync
      description: Instalar dependencias Python

    - cmd: maturin develop
      description: Compilar módulo Rust y vincularlo al entorno Python activo

  run:
    - cmd: uv run python -m pycalc.ui.app
      description: Ejecutar la aplicación

  test:
    - cmd: uv run pytest --cov=pycalc --cov-report=term-missing
      description: Correr todos los tests con reporte de cobertura

  lint:
    - cmd: uv run ruff check .
      description: Verificar estilo Python
    - cmd: uv run ruff format .
      description: Formatear código Python
    - cmd: cargo clippy -- -D warnings
      description: Linting Rust
    - cmd: cargo fmt
      description: Formatear código Rust

  build:
    - cmd: maturin build --release
      description: Compilar módulo Rust optimizado para distribución
```

---

## Reglas de Contribución

```yaml
contribution:
  branch_strategy: feature branches desde main
  commit_format: "tipo(scope): descripción"
  commit_types: [feat, fix, refactor, test, docs, chore]

  rules:
    - No usar unwrap() en Rust sin comentario justificado
    - Tests obligatorios para toda función nueva en core/ y services/
    - Cobertura mínima 80% antes de merge
    - Linting sin errores antes de commit
    - Estilos visuales solo en theme.py

  review_checklist:
    - "[ ] Tests escritos y pasando"
    - "[ ] Cobertura >= 80%"
    - "[ ] ruff check sin errores"
    - "[ ] cargo clippy sin warnings"
    - "[ ] project.md actualizado si hubo cambios de arquitectura"
```

---

## Roadmap

```yaml
roadmap:
  v0.1.0:
    status: in_progress
    features:
      - Operaciones básicas (suma, resta, multiplicación, división)
      - Módulo Rust compilado con PyO3
      - Interfaz Flet funcional

  v0.2.0:
    status: planned
    features:
      - Operaciones avanzadas (potencia, raíz, módulo)
      - Historial de operaciones en UI
      - Soporte de teclado físico

  v0.3.0:
    status: planned
    features:
      - Modo científico
      - Tema claro/oscuro
      - Build para distribución (empaquetado multiplataforma)
```
