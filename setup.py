from setuptools import setup, find_packages

setup(
    name="{{ package_name }}",
    version="0.1.0",
    author="{{ author_name }}",
    description="{{ description }}",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=open("requirements.txt").read().splitlines(),
)