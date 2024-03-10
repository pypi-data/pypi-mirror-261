from setuptools import setup, find_packages

setup(
    name="WaterMoleculeClassifier",
    version="0.12",
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['models/*.joblib']},
    install_requires=[
        "joblib",
        "scikit-learn",
        "pandas"
    ],
)
