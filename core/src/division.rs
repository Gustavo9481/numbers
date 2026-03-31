use pyo3::prelude::*;

#[pyfunction]
pub fn divide(a: f64, b: f64) -> PyResult<f64> {
    if b == 0.0 {
        Err(pyo3::exceptions::PyZeroDivisionError::new_err(
            "Division by zero",
        ))
    } else {
        Ok(a / b)
    }
}
