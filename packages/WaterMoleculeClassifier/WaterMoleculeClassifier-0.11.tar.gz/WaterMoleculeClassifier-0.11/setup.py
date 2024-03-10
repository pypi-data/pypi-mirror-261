from setuptools import setup, find_packages

setup(
    name="WaterMoleculeClassifier",
    version="0.11",
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['models/*.pkl']},
    install_requires=[
        "joblib",
        "scikit-learn",
        "pandas"
    ],
)
