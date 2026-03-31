//! Módulo de cálculo de porcentaje.

use pyo3::prelude::*;

/// Calcula el porcentaje de un valor sobre un total.
#[pyfunction]
pub fn percentage(value: f64, total: f64) -> f64 {
    value * total / 100.0
}
