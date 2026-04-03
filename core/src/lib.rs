use pyo3::prelude::*;

// Módulos internos
mod suma;
mod resta;
mod multiplicacion;
mod division;
mod porcentaje;

#[pyfunction]
pub fn sumar(numbers: Vec<f64>) -> f64 {
    suma::execute(numbers)
}

#[pyfunction]
pub fn subtract(numbers: Vec<f64>) -> f64 {
    resta::execute(numbers)
}

#[pyfunction]
pub fn multiply(numbers: Vec<f64>) -> f64 {
    multiplicacion::execute(numbers)
}

#[pyfunction]
pub fn divide(numbers: Vec<f64>) -> PyResult<f64> {
    division::execute(numbers).map_err(|e| match e {
        division::DivisionError::DivideByZero => {
            pyo3::exceptions::PyZeroDivisionError::new_err(e.to_string())
        }
    })
}

#[pyfunction]
pub fn percentage(value: f64, total: f64) -> f64 {
    porcentaje::execute(value, total)
}

#[pymodule]
fn pycalc_core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sumar, m)?)?;
    m.add_function(wrap_pyfunction!(subtract, m)?)?;
    m.add_function(wrap_pyfunction!(multiply, m)?)?;
    m.add_function(wrap_pyfunction!(divide, m)?)?;
    m.add_function(wrap_pyfunction!(percentage, m)?)?;
    Ok(())
}
