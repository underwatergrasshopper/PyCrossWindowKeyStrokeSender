from setuptools import setup, find_packages
from pathlib import Path


PROJECT_PATH = Path(__file__).parent.resolve()

NAME                = "PyCrossWindowKeyStrokeSender"
VERSION             = (PROJECT_PATH / "src" / NAME / "version").read_text("utf-8").strip()
LONG_DESCRIPTION    = (PROJECT_PATH / "README.md").read_text("utf-8")


setup(
    name                            = NAME, 
    version                         = VERSION,
    author                          = "underwatergrasshopper",
    description                     = "Simple library for sending keystrokes to chosen window.",
    long_description                = LONG_DESCRIPTION,
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
    package_dir                     = {"" : "src"},
    packages                        = find_packages(where = "src"),
    package_data                    = {NAME : ["version"]},
    license                         = "MIT",
    python_requires                 = "==3.11.*",
)