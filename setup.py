from setuptools import find_namespace_packages, setup


def read_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="test",
    version="0.1",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    install_requires=read_requirements("requirements.txt"),
)
