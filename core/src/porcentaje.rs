//! Módulo de cálculo de porcentaje.

/// Calcula el porcentaje de un valor sobre un total.
pub fn execute(value: f64, total: f64) -> f64 {
    value * total / 100.0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_percentage_standard() {
        assert_eq!(execute(50.0, 200.0), 100.0);
    }

    #[test]
    fn test_percentage_zero_value() {
        assert_eq!(execute(0.0, 100.0), 0.0);
    }

    #[test]
    fn test_percentage_zero_total() {
        assert_eq!(execute(100.0, 0.0), 0.0);
    }
}

