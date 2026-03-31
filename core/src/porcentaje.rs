use pyo3::prelude::*;

#[pyfunction]
pub fn percentage(value: f64, total: f64) -> f64 {
    value * total / 100.0
}
