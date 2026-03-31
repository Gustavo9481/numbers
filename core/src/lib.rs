//! # PyCalc Core
//!
//! Este módulo proporciona las funciones principales para operaciones matemáticas
//! básicas y avanzadas expuestas a Python a través de PyO3.

mod division;
mod multiplicacion;
mod porcentaje;
mod resta;
mod suma;

use pyo3::prelude::*;

/// Suma dos números de punto flotante.
#[pyfunction]
pub fn add(a: f64, b: f64) -> f64 {
    suma::add(a, b)
}

/// Resta el segundo número del primero.
#[pyfunction]
pub fn subtract(a: f64, b: f64) -> f64 {
    resta::subtract(a, b)
}

/// Multiplica dos números de punto flotante.
#[pyfunction]
pub fn multiply(a: f64, b: f64) -> f64 {
    multiplicacion::multiply(a, b)
}

/// Divide el primer número por el segundo.
///
/// # Errores
///
/// Retorna un `PyZeroDivisionError` si el divisor es 0.0.
#[pyfunction]
pub fn divide(a: f64, b: f64) -> PyResult<f64> {
    division::divide(a, b)
}

/// Calcula el porcentaje de un valor dado un total.
///
/// El resultado es `(value * total) / 100`.
#[pyfunction]
pub fn percentage(value: f64, total: f64) -> f64 {
    porcentaje::percentage(value, total)
}

/// Definición del módulo de Python `pycalc_core`.
#[pymodule]
fn pycalc_core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add, m)?)?;
    m.add_function(wrap_pyfunction!(subtract, m)?)?;
    m.add_function(wrap_pyfunction!(multiply, m)?)?;
    m.add_function(wrap_pyfunction!(divide, m)?)?;
    m.add_function(wrap_pyfunction!(percentage, m)?)?;
    Ok(())
}
