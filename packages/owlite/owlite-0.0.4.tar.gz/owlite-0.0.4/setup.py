import sys
from setuptools import setup

ACTION: str = sys.argv[1]
PACKAGE_VERSION: str = "0.0.4"

ERROR_MSG: str = r"""


################################################################################################
The package you are trying to install is only a placeholder project on PyPI.org repository.
This package is hosted on SqueezeBits Python Package Index.

This package can be installed as:
```
$ pip install owlite --extra-index-url https://pypi.squeezebits.com/
```

Please visit us at www.squeezebits.com or github.com/SqueezeBits/Owlite for further information.
################################################################################################


"""

def main():

    with open('README.md') as f:
        long_description = f.read()

    setup(
        name="owlite",
        version=PACKAGE_VERSION,
        long_description=long_description,
        long_description_content_type="text/markdown",
        description="A fake package to warn the user they are not installing the correct package.",
        url="https://github.com/SqueezeBits/owlite",
        author="SqueezeBits Inc.",
        author_email="owlite@squeezebits.com",
        python_requires="~=3.10.0",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3.10",
            "Topic :: Scientific/Engineering",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Software Development",
            "Topic :: Software Development :: Libraries",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        keywords=["torch", "onnx", "graph", "quantization", "owlite"],
    )


if ACTION == "sdist":
    main()
else:
    raise RuntimeError(ERROR_MSG)
