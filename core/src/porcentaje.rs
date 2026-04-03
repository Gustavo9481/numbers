//! Módulo de cálculo de porcentaje.

/// Calcula el porcentaje de un valor sobre un total.
pub fn execute(value: f64, total: f64) -> f64 {
    value * total / 100.0
}
