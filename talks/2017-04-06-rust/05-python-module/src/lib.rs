#[macro_use]
extern crate cpython;
use std::collections::HashMap;

use cpython::{PyResult, Python, PyString};

py_module_initializer!(libpython_module,
                       initpython_module,
                       PyInit_python_module,
                       |py, m| {
    try!(m.add(py, "__doc__", "This module is implemented in Rust."));
    try!(m.add(py,
               "word_count",
               py_fn!(py, word_count_py(text: PyString))));
    Ok(())
});

fn word_count_py(py: Python,
                 text: PyString)
                 -> PyResult<HashMap<String, u64>> {
    let s = text.to_string(py)?;
    Ok(word_count(s.into_owned()))
}

pub fn word_count(s: String) -> HashMap<String, u64> {
    let mut counts = HashMap::new();
    for word in s.split_whitespace() {
        if word.len() < 5 {
            continue;
        }
        let lower = word.to_lowercase();
        *counts.entry(String::from(lower)).or_insert(0) += 1;
    }
    counts
}
