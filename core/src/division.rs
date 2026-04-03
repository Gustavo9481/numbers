//! Módulo de división.

use thiserror::Error;

#[derive(Error, Debug)]
pub enum DivisionError {
    #[error("Division by zero in sequence")]
    DivideByZero,
}

/// Divide secuencialmente los elementos de una lista `f64`.
pub fn execute(numbers: Vec<f64>) -> Result<f64, DivisionError> {
    let mut iter = numbers.iter();
    let first = match iter.next() {
        Some(&v) => v,
        None => return Ok(0.0),
    };

    let mut result = first;
    for &val in iter {
        if val == 0.0 {
            return Err(DivisionError::DivideByZero);
        }
        result /= val;
    }

    Ok(result)
}
