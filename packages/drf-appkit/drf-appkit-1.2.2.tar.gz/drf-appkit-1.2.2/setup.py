from setuptools import setup, find_packages

setup(
    packages=find_packages(where="appkit"),
    package_dir={"": "appkit"},
    include_package_data=True,
)
