//! Módulo de resta.

use pyo3::prelude::*;

/// Resta el segundo número del primero.
#[pyfunction]
pub fn subtract(a: f64, b: f64) -> f64 {
    a - b
}
