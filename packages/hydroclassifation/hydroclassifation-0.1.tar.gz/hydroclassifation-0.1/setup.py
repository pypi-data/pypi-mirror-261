from setuptools import setup, find_packages

setup(
    name="hydroclassifation",
    version="0.1",
    description="Package for hydrogeological classifcation",
    author="Brayan A. Quiceno",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
    ],
)
