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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_divide_multiple_values() {
        let numbers = vec![100.0, 2.0, 5.0];
        assert_eq!(execute(numbers).unwrap(), 10.0);
    }

    #[test]
    fn test_divide_by_zero() {
        let numbers = vec![100.0, 0.0, 5.0];
        let res = execute(numbers);
        assert!(matches!(res, Err(DivisionError::DivideByZero)));
    }

    #[test]
    fn test_divide_single_value() {
        let numbers = vec![42.0];
        assert_eq!(execute(numbers).unwrap(), 42.0);
    }

    #[test]
    fn test_divide_empty() {
        let numbers = vec![];
        assert_eq!(execute(numbers).unwrap(), 0.0);
    }
}

