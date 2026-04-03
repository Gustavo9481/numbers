## Context

El proyecto `numbers` utiliza una arquitectura híbrida donde Rust realiza los cálculos pesados. Actualmente, las funciones core solo aceptan dos operandos. Para escalar hacia una calculadora profesional, necesitamos que esta capa de bajo nivel sea capaz de procesar colecciones de datos, reduciendo el overhead de comunicación entre lenguajes y simplificando la lógica de la UI.

## Goals / Non-Goals

**Goals:**
- Refactorizar el motor de Rust para procesar `Vec<f64>` en suma, resta, multiplicación y división.
- Utilizar iteradores nativos de Rust para garantizar el máximo rendimiento.
- Adaptar la capa de servicios de Python para ofrecer una API flexible mediante `*args`.
- Actualizar la suite de pruebas para cubrir casos de múltiples valores y listas vacías.

**Non-Goals:**
- No se incluirán operaciones científicas avanzadas (raíz cuadrada, potencias) en este ciclo de cambio.
- No se modificará el tipo de dato base (`f64`) por `Decimal`.

## Decisions

- **Estrategia de Iteración**: Se utilizarán los métodos `iter().sum()` e `iter().product()` para suma y multiplicación por ser altamente optimizados por el compilador de Rust.
- **Lógica de Resta**: Para una lista $[v_0, v_1, ..., v_n]$, el resultado será $v_0 - (v_1 + ... + v_n)$. Si la lista tiene un solo elemento, retorna dicho elemento.
- **Lógica de División**: Se procesará secuencialmente $v_0 / v_1 / ... / v_n$. Se debe validar que ningún elemento a partir de $v_1$ sea cero.
- **API Python (Symmetry)**: El `CalculatorService` expondrá métodos que acepten `*args`, pero internamente los convertirá a `list` para el motor de Rust, manteniendo la facilidad de uso sin perder la capacidad de procesar colecciones preexistentes.

## Risks / Trade-offs

- **[Riesgo] Listas Vacías** → **Mitigación**: El servicio de Python validará que al menos haya un valor (para suma/resta/multi) o dos (para división) antes de llamar a Rust, o Rust devolverá valores neutros (0.0 para suma, 1.0 para multi).
- **[Riesgo] Precisión en Divisiones Largas** → **Mitigación**: El uso de `f64` es suficiente para los requerimientos de la calculadora, pero se documentará que la precisión puede variar ligeramente en cadenas largas de divisiones.
