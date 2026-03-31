## Context

El proyecto PyCalc necesita un módulo core en Rust que maneje la lógica matemática. Este módulo será la base de la calculadora y debe ser expuesto a Python via PyO3. El estado actual es v0.1.0 en progreso según project.md.

## Goals / Non-Goals

**Goals:**
- Crear 5 funciones matemáticas en Rust: suma, resta, multiplicación, división, porcentaje
- Exponer funciones a Python usando macros PyO3 #[pyfunction]
- Implementar manejo de errores para división por cero
- Crear tests unitarios con pytest cubriendo casos límite

**Non-Goals:**
- UI de la calculadora (capa services y UI)
- Operaciones avanzadas (potencia, raíz cuadrada, módulo) - estas van en v0.2.0
- Historial de operaciones
- Tema oscuro/claro

## Decisiones

1. **Estructura de archivos**: Cada función en archivo individual importado desde lib.rs
   - Razón: Propuesto en propose_1.md, facilita mantenimiento y testing
   - Alternativa: Todo en un solo archivo - descartado por menor claridad

2. **Manejo de errores**: Usar thiserror para errores custom
   - Razón: Proporciona implementación derive macros simple y compatible con PyO3
   - Alternativa: Manejo manual con Result - más verboso

3. **Tipo de datos**: Usar f64 para todas las operaciones
   - Razón: Precisión suficiente para calculadora básica y compatible con Python float
   - Alternativa: i32 - limitante para decimales

## Risks / Trade-offs

- [Risk] División por cero → [Mitigation] Retornar error usando thiserror
- [Risk] Errores de compilación PyO3 → [Mitigation] Verificar versiones compatibles en Cargo.toml
- [Risk] Testing con pytest requiere módulo compilado → [Mitigation] Usar maturin develop antes de tests
