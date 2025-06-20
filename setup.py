from setuptools import setup, find_packages
from pathlib import Path


PROJECT_PATH = Path(__file__).parent.resolve()

long_description = (PROJECT_PATH / "README.md").read_text(encoding="utf-8")


setup(
    name                            = "PyCrossWindowKeyStrokeSender", 
    version                         = "0.1.5+dev",
    author                          = "underwatergrasshopper",
    description                     = "Simple library for sending keystrokes to chosen window.",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",

    url                             = "https://github.com/underwatergrasshopper/PyCrossWindowKeyStrokeSender",
    project_urls                    = {
        "Bug Tracker": "https://github.com/underwatergrasshopper/PyCrossWindowKeyStrokeSender/issues",
    },
    classifiers                     = [
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    package_dir                     = {"": "src"},
    packages                        = find_packages(where = "src"),
    install_requires                = [],
    license                         = "MIT",
    python_requires                 = "==3.11.*",
)