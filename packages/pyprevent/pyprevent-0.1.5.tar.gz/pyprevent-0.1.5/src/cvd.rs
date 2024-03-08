use crate::covariates::Covariates;
use crate::utils::{calculate_risk_rust_parallel_np, common_calculation, validate_input};
use numpy::PyReadonlyArrayDyn;
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use std::f64;
use std::f64::consts::E;

pub fn calculate_10_yr_cvd_risk(
    sex: &str,
    age: f64,
    total_cholesterol: f64,
    hdl_cholesterol: f64,
    systolic_bp: f64,
    has_diabetes: bool,
    current_smoker: bool,
    bmi: f64,
    egfr: f64,
    on_htn_meds: bool,
    on_cholesterol_meds: bool,
) -> Result<f64, String> {
    validate_input(
        age,
        total_cholesterol,
        hdl_cholesterol,
        systolic_bp,
        bmi,
        egfr,
        true,
    )?;

    let cholesterol_diff = total_cholesterol - hdl_cholesterol;
    let adjusted_age = (age - 55.0) / 10.0;
    let adjusted_age_squared = adjusted_age.powi(2);

    match sex.to_lowercase().as_str() {
        "female" => {
            let covariates = Covariates::female_10_yr_cvd();
            let calculation = common_calculation(
                &covariates,
                has_diabetes,
                current_smoker,
                on_htn_meds,
                on_cholesterol_meds,
                systolic_bp,
                cholesterol_diff,
                hdl_cholesterol,
                adjusted_age,
                adjusted_age_squared,
                egfr,
                bmi,
            );
            let risk_score = E.powf(calculation) / (1.0 + E.powf(calculation)) * 100.0;
            Ok(risk_score)
        }
        "male" => {
            let covariates = Covariates::male_10_yr_cvd();
            let calculation = common_calculation(
                &covariates,
                has_diabetes,
                current_smoker,
                on_htn_meds,
                on_cholesterol_meds,
                systolic_bp,
                cholesterol_diff,
                hdl_cholesterol,
                adjusted_age,
                adjusted_age_squared,
                egfr,
                0.0,
            );
            let risk_score = E.powf(calculation) / (1.0 + E.powf(calculation)) * 100.0;
            Ok(risk_score)
        }
        _ => Err("Sex must be either 'male' or 'female'.".to_string()),
    }
}

pub fn calculate_30_yr_cvd_risk(
    sex: &str,
    age: f64,
    total_cholesterol: f64,
    hdl_cholesterol: f64,
    systolic_bp: f64,
    has_diabetes: bool,
    current_smoker: bool,
    bmi: f64,
    egfr: f64,
    on_htn_meds: bool,
    on_cholesterol_meds: bool,
) -> Result<f64, String> {
    validate_input(
        age,
        total_cholesterol,
        hdl_cholesterol,
        systolic_bp,
        bmi,
        egfr,
        false,
    )?;

    let cholesterol_difference = total_cholesterol - hdl_cholesterol;
    let age_factor = (age - 55.0) / 10.0;
    let age_squared = age_factor.powi(2);

    match sex.to_lowercase().as_str() {
        "female" => {
            let covariates = Covariates::female_30_yr_cvd();
            let calculation = common_calculation(
                &covariates,
                has_diabetes,
                current_smoker,
                on_htn_meds,
                on_cholesterol_meds,
                systolic_bp,
                cholesterol_difference,
                hdl_cholesterol,
                age_factor,
                age_squared,
                egfr,
                0.0,
            );
            let risk_score = E.powf(calculation) / (1.0 + E.powf(calculation)) * 100.0;
            Ok(risk_score)
        }
        "male" => {
            let covariates = Covariates::male_30_yr_cvd();
            let calculation = common_calculation(
                &covariates,
                has_diabetes,
                current_smoker,
                on_htn_meds,
                on_cholesterol_meds,
                systolic_bp,
                cholesterol_difference,
                hdl_cholesterol,
                age_factor,
                age_squared,
                egfr,
                0.0,
            );
            let risk_score = E.powf(calculation) / (1.0 + E.powf(calculation)) * 100.0;
            Ok(risk_score)
        }
        _ => Err("Sex must be either 'male' or 'female'.".to_string()),
    }
}

#[pyfunction]
pub fn calculate_10_yr_cvd_rust(
    sex: String,
    age: f64,
    total_cholesterol: f64,
    hdl_cholesterol: f64,
    systolic_bp: f64,
    has_diabetes: bool,
    current_smoker: bool,
    bmi: f64,
    egfr: f64,
    on_htn_meds: bool,
    on_cholesterol_meds: bool,
) -> PyResult<f64> {
    match calculate_10_yr_cvd_risk(
        &sex,
        age,
        total_cholesterol,
        hdl_cholesterol,
        systolic_bp,
        has_diabetes,
        current_smoker,
        bmi,
        egfr,
        on_htn_meds,
        on_cholesterol_meds,
    ) {
        Ok(value) => Ok(value),
        Err(e) => Err(PyValueError::new_err(e)), // Convert Rust String error to Python ValueError
    }
}

#[pyfunction]
pub fn calculate_30_yr_cvd_rust(
    sex: String,
    age: f64,
    total_cholesterol: f64,
    hdl_cholesterol: f64,
    systolic_bp: f64,
    has_diabetes: bool,
    current_smoker: bool,
    bmi: f64,
    egfr: f64,
    on_htn_meds: bool,
    on_cholesterol_meds: bool,
) -> PyResult<f64> {
    match calculate_30_yr_cvd_risk(
        &sex,
        age,
        total_cholesterol,
        hdl_cholesterol,
        systolic_bp,
        has_diabetes,
        current_smoker,
        bmi,
        egfr,
        on_htn_meds,
        on_cholesterol_meds,
    ) {
        Ok(value) => Ok(value),
        Err(e) => Err(PyValueError::new_err(e)), // Convert Rust String error to Python ValueError
    }
}

#[pyfunction]
pub fn calculate_10_yr_cvd_rust_parallel_np(
    py: Python,
    data: PyReadonlyArrayDyn<f64>,
) -> PyResult<PyObject> {
    calculate_risk_rust_parallel_np(py, data, calculate_10_yr_cvd_risk)
}

#[pyfunction]
pub fn calculate_30_yr_cvd_rust_parallel_np(
    py: Python,
    data: PyReadonlyArrayDyn<f64>,
) -> PyResult<PyObject> {
    calculate_risk_rust_parallel_np(py, data, calculate_30_yr_cvd_risk)
}
