from setuptools import setup
from setuptools_rust import RustExtension

python_module = RustExtension('python_module', 'Cargo.toml')

setup(
    name='test',
    version='1.0',
    rust_extensions=[python_module],
    # Rust extensions are not zip safe, just like C extensions
    zip_safe=False)
