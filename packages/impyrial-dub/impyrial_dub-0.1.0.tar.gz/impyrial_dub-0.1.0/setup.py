# Import required functions
from setuptools import setup, find_packages

# Call setup function
setup(
    author="ahmet yasin tat",
    description="A package for converting imperial lengths and weights.",
    name="impyrial_dub",
    packages=find_packages(include=["impyrial_dub","impyrial_dub.*"]),
    version="0.1.0",
    install_requires=["numpy", "pandas","matplotlib","scipy","sklearn"],
)
