from setuptools import setup, find_packages

setup(
    name="hydroclassification",
    version="0.4",
    description="Package for hydrogeological classifcation",
    author="Brayan A. Quiceno",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
    ],
)
