from setuptools import setup, find_packages

setup(
    name="hygeoclas",
    version="0.2",
    description="Package for hydrogeological classifcation",
    author="Brayan A. Quiceno",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "torch"
    ],
)
