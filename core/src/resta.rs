//! Módulo de resta.

/// Resta secuencialmente los elementos de una lista `f64`.
pub fn execute(numbers: Vec<f64>) -> f64 {
    let mut iter = numbers.iter();
    match iter.next() {
        Some(&first) => first - iter.sum::<f64>(),
        None => 0.0,
    }
}
