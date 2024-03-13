from setuptools import setup

name = "types-PyScreeze"
description = "Typing stubs for PyScreeze"
long_description = '''
## Typing stubs for PyScreeze

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`PyScreeze`](https://github.com/asweigart/pyscreeze) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`PyScreeze`.

This version of `types-PyScreeze` aims to provide accurate annotations
for `PyScreeze==0.1.30`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/PyScreeze. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `8a9dcb1967b99600ced8eb4fa6c07df686d09697` and was tested
with mypy 1.9.0, pyright 1.1.350, and
pytype 2024.2.27.
'''.lstrip()

setup(name=name,
      version="0.1.30.20240313",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/PyScreeze.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['types-Pillow'],
      packages=['pyscreeze-stubs'],
      package_data={'pyscreeze-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
