from setuptools import setup

setup(
    name='example-03-package-main',
    version='1.0.0.dev0',
    packages=['report'],
    entry_points = {
        'console_scripts': ['report=report.__main__:main'],
    }
)
