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
               py_fn!(py, word_count(text: PyString))));
    Ok(())
});

fn word_count(py: Python,
              text: PyString)
              -> PyResult<HashMap<String, u64>> {
    let s = text.to_string(py)?;
    let mut counts = HashMap::new();

    for word in s.split_whitespace() {
        if word.len() < 5 {
            continue;
        }
        let lower = word.to_lowercase();
        *counts.entry(String::from(lower)).or_insert(0) += 1;
    }
    Ok(counts)
}
