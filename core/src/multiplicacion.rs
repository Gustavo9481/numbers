use pyo3::prelude::*;

#[pyfunction]
pub fn multiply(a: f64, b: f64) -> f64 {
    a * b
}
