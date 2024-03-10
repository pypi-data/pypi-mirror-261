from setuptools import setup

name = "types-inifile"
description = "Typing stubs for inifile"
long_description = '''
## Typing stubs for inifile

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`inifile`](https://github.com/mitsuhiko/python-inifile) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`inifile`.

This version of `types-inifile` aims to provide accurate annotations
for `inifile==0.4.*`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/inifile. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `f94bbfbcc4c3b2b289425ea793beda0822e702f8` and was tested
with mypy 1.9.0, pyright 1.1.350, and
pytype 2024.2.27.
'''.lstrip()

setup(name=name,
      version="0.4.0.20240310",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/inifile.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['inifile-stubs'],
      package_data={'inifile-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
