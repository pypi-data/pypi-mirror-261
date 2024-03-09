//  This Source Code Form is subject to the terms of the Mozilla Public
//  License, v. 2.0. If a copy of the MPL was not distributed with this
//  file, You can obtain one at http://mozilla.org/MPL/2.0/.

use amora_rs;
use x25519_dalek::{PublicKey, StaticSecret};
use pyo3::prelude::*;
use pyo3::PyResult;
use pyo3::exceptions::PyValueError;

#[pymodule]
fn amora_py(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
	m.add_class::<AmoraVer>()?;
	m.add_class::<Amora>()?;
	m.add_class::<AmoraMeta>()?;
	Ok(())
}

#[pyclass]
enum AmoraVer {
	Zero = amora_rs::AmoraVer::Zero as isize,
	One = amora_rs::AmoraVer::One as isize,
}

#[pyclass]
struct Amora {
	amora: amora_rs::Amora,
}

#[pyclass]
struct AmoraMeta {
	meta: amora_rs::AmoraMeta,
}

#[pymethods]
impl Amora {
	#[staticmethod]
	fn amora_zero(key: [u8; 32]) -> Amora {
		let amora = amora_rs::Amora::amora_zero(&key);
		Amora { amora: amora }
	}

	#[staticmethod]
	fn amora_one(secret_key: Option<[u8; 32]>, public_key: Option<[u8; 32]>) -> Amora {
		let secret_key: Option<StaticSecret> = match secret_key {
			Some(key) => Some(StaticSecret::from(key)),
			None => None,
		};

		let public_key: Option<PublicKey> = match public_key {
			Some(key) => Some(PublicKey::from(key)),
			None => None,
		};

		let amora = amora_rs::Amora::amora_one(secret_key, public_key);
		Amora { amora: amora }
	}

	#[staticmethod]
	fn amora_zero_from_str(key: &str) -> PyResult<Amora> {
		match amora_rs::Amora::amora_zero_from_str(key) {
			Ok(amora) => Ok(Amora { amora: amora }),
			Err(error) => Err(PyValueError::new_err(format!("{:?}", error))),
		}
	}

	#[staticmethod]
	fn amora_one_from_str(secret_key: Option<&str>, public_key: Option<&str>)
		-> PyResult<Amora> {

		match amora_rs::Amora::amora_one_from_str(secret_key, public_key) {
			Ok(amora) => Ok(Amora { amora: amora }),
			Err(error) => Err(PyValueError::new_err(format!("{:?}", error))),
		}
	}

	fn encode(&self, payload: &[u8], ttl: u32) -> String {
		self.amora.encode(payload, ttl)
	}

	fn decode(&self, token: &str, validate: bool) -> PyResult<Vec<u8>> {
		match self.amora.decode(token, validate) {
			Ok(decoded) => Ok(decoded),
			Err(error) => Err(PyValueError::new_err(format!("{:?}", error))),
		}
	}

	#[staticmethod]
	fn meta(token: &str) -> PyResult<AmoraMeta> {
		match amora_rs::Amora::meta(token) {
			Ok(meta) => Ok(AmoraMeta { meta }),
			Err(error) => Err(PyValueError::new_err(format!("{:?}", error))),
		}
	}
}

#[pymethods]
impl AmoraMeta {
	#[getter]
	fn version(&self) -> AmoraVer {
		match self.meta.version {
			amora_rs::AmoraVer::Zero => AmoraVer::Zero,
			amora_rs::AmoraVer::One => AmoraVer::One,
		}
	}

	#[getter]
	fn ttl(&self) -> u32 {
		self.meta.ttl
	}

	#[getter]
	fn timestamp(&self) -> u32 {
		self.meta.timestamp
	}

	#[getter]
	fn is_valid(&self) -> bool {
		self.meta.is_valid
	}

	fn __str__(&self) -> PyResult<String> {
		Ok(format!("{:?}", self.meta))
	}
}
