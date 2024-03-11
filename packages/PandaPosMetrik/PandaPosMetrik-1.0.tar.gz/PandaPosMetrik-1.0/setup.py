from setuptools import setup

setup(
    name="PandaPosMetrik",
    version="1.0",
    packages=["Metrik"],
    include_package_data=True,
    install_requires=[
        
        "pyodbc",
    ]
)
