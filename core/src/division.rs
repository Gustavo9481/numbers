//! Módulo de división.

use pyo3::prelude::*;

/// Divide secuencialmente los elementos de una lista `f64`.
pub fn execute(numbers: Vec<f64>) -> PyResult<f64> {
    let mut iter = numbers.iter();
    let first = match iter.next() {
        Some(&v) => v,
        None => return Ok(0.0),
    };

    let mut result = first;
    for &val in iter {
        if val == 0.0 {
            return Err(pyo3::exceptions::PyZeroDivisionError::new_err(
                "Division by zero in sequence",
            ));
        }
        result /= val;
    }

    Ok(result)
}
