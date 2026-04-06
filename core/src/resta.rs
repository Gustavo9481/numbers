//! Módulo de resta.

/// Resta secuencialmente los elementos de una lista `f64`.
pub fn execute(numbers: Vec<f64>) -> f64 {
    let mut iter = numbers.iter();
    match iter.next() {
        Some(&first) => first - iter.sum::<f64>(),
        None => 0.0,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_resta_multiple_values() {
        let numbers = vec![100.0, 20.0, 10.0];
        assert_eq!(execute(numbers), 70.0);
    }

    #[test]
    fn test_resta_single_value() {
        let numbers = vec![42.0];
        assert_eq!(execute(numbers), 42.0);
    }

    #[test]
    fn test_resta_empty() {
        let numbers = vec![];
        assert_eq!(execute(numbers), 0.0);
    }
}

