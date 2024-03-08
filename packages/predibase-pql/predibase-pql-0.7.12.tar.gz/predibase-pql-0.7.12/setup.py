from codecs import open
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line]

version = {}
with open(path.join(here, "predibase_pql", "version.py")) as fp:
    exec(fp.read(), version)

setup(
    name='predibase-pql',
    version=version["__version__"],
    description="Predibase PQL client and proto definition.",
    author='Predibase Inc.',
    packages=find_packages(),
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    extras_require={
        "notebook": ["notebook", "jupyterlab", "dask-sql", "python-graphviz"],
    },
)
