//! Módulo de multiplicación.

/// Multiplica una lista de números `f64`.
pub fn execute(numbers: Vec<f64>) -> f64 {
    if numbers.is_empty() {
        return 0.0;
    }
    numbers.iter().product()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_multiply_multiple_values() {
        let numbers = vec![2.0, 3.0, 4.0];
        assert_eq!(execute(numbers), 24.0);
    }

    #[test]
    fn test_multiply_single_value() {
        let numbers = vec![42.0];
        assert_eq!(execute(numbers), 42.0);
    }

    #[test]
    fn test_multiply_empty() {
        let numbers = vec![];
        assert_eq!(execute(numbers), 0.0);
    }
}

