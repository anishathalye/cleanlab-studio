from setuptools import setup
from config import __version__
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="cleanlab-cli",
    version=__version__,
    author="Cleanlab, Inc.",
    author_email="team@cleanlab.ai",
    description="Command line interface for all things Cleanlab Studio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cleanlab/cleanlab-cli",
    project_urls={
        "Bug Tracker": "https://github.com/cleanlab/cleanlab-cli/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords="cleanlab",
    packages=["cleanlab_cli"],
    py_modules=["main"],
    python_requires=">=3.7",
    install_requires=[
        "Click>=8.0.4",
        "colorama>=0.4.4",
        "pandas>=1.4.1",
        "pyexcel>=0.7.0",
        "pyexcel-xls>=0.7.0",
        "pyexcel-xlsx>=0.6.0",
        "requests>=2.27.1",
        "tqdm>=4.64.0",
        "ijson>=3.1.4",
    ],
    entry_points="""
        [console_scripts]
        cleanlab=cleanlab_cli.main:cli
    """,
)
