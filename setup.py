import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name                            = "PyCrossWindowKeyStrokeSender",
    version                         = "0.1.3",
    author                          = "underwatergrasshopper",
    author_email                    = "",
    description                     = "Simple library for sending keystrokes to chosen window.",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    url                             = "https://github.com/underwatergrasshopper/PyCrossWindowKeyStrokeSender",
    project_url                     = {
        "Bug Tracker": "https://github.com/underwatergrasshopper/PyCrossWindowKeyStrokeSender/issues",
    },
    classifiers                     = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    package_dir                     = {"": "src"},
    packages                        = setuptools.find_packages(where = "src"),
    install_requires                = [],
    license                         = "MIT",
    python_requires                 = ">=3.9",
)