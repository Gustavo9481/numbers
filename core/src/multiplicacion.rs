//! Módulo de multiplicación.

use pyo3::prelude::*;

/// Multiplica dos números `f64`.
#[pyfunction]
pub fn multiply(a: f64, b: f64) -> f64 {
    a * b
}
