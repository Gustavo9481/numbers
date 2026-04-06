//! Módulo de suma.

/// Suma una lista de números `f64`.
pub fn execute(numbers: Vec<f64>) -> f64 {
    numbers.iter().sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_suma_multiple_values() {
        let numbers = vec![1.0, 2.0, 3.5];
        assert_eq!(execute(numbers), 6.5);
    }

    #[test]
    fn test_suma_single_value() {
        let numbers = vec![42.0];
        assert_eq!(execute(numbers), 42.0);
    }

    #[test]
    fn test_suma_empty() {
        let numbers = vec![];
        assert_eq!(execute(numbers), 0.0);
    }
}

