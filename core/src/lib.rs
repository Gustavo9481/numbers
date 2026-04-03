use pyo3::prelude::*;

#[pyfunction]
pub fn sumar(numbers: Vec<f64>) -> f64 {
    numbers.iter().sum()
}

#[pyfunction]
pub fn subtract(numbers: Vec<f64>) -> f64 {
    let mut iter = numbers.iter();
    match iter.next() {
        Some(&first) => first - iter.sum::<f64>(),
        None => 0.0,
    }
}

#[pyfunction]
pub fn multiply(numbers: Vec<f64>) -> f64 {
    if numbers.is_empty() {
        return 0.0;
    }
    numbers.iter().product()
}

#[pyfunction]
pub fn divide(numbers: Vec<f64>) -> PyResult<f64> {
    let mut iter = numbers.iter();
    let first = match iter.next() {
        Some(&v) => v,
        None => return Ok(0.0),
    };

    let mut result = first;
    for &val in iter {
        if val == 0.0 {
            return Err(pyo3::exceptions::PyZeroDivisionError::new_err(
                "Division by zero in sequence",
            ));
        }
        result /= val;
    }
    Ok(result)
}

#[pyfunction]
pub fn percentage(value: f64, total: f64) -> f64 {
    value * total / 100.0
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
