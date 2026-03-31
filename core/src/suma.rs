//! Módulo de suma.

use pyo3::prelude::*;

/// Suma dos números `f64`.
#[pyfunction]
pub fn add(a: f64, b: f64) -> f64 {
    a + b
}
