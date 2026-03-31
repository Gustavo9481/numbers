mod division;
mod multiplicacion;
mod porcentaje;
mod resta;
mod suma;

use pyo3::prelude::*;

#[pyfunction]
pub fn add(a: f64, b: f64) -> f64 {
    suma::add(a, b)
}

#[pyfunction]
pub fn subtract(a: f64, b: f64) -> f64 {
    resta::subtract(a, b)
}

#[pyfunction]
pub fn multiply(a: f64, b: f64) -> f64 {
    multiplicacion::multiply(a, b)
}

#[pyfunction]
pub fn divide(a: f64, b: f64) -> PyResult<f64> {
    division::divide(a, b)
}

#[pyfunction]
pub fn percentage(value: f64, total: f64) -> f64 {
    porcentaje::percentage(value, total)
}

#[pymodule]
fn pycalc_core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add, m)?)?;
    m.add_function(wrap_pyfunction!(subtract, m)?)?;
    m.add_function(wrap_pyfunction!(multiply, m)?)?;
    m.add_function(wrap_pyfunction!(divide, m)?)?;
    m.add_function(wrap_pyfunction!(percentage, m)?)?;
    Ok(())
}
