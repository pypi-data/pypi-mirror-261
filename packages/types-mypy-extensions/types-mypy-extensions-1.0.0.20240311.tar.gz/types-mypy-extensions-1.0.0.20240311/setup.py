from setuptools import setup

name = "types-mypy-extensions"
description = "Typing stubs for mypy-extensions"
long_description = '''
## Typing stubs for mypy-extensions

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`mypy-extensions`](https://github.com/python/mypy_extensions) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`mypy-extensions`.

This version of `types-mypy-extensions` aims to provide accurate annotations
for `mypy-extensions==1.0.*`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/mypy-extensions. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `3802899a01269df575ea32a21534c5400fb9218a` and was tested
with mypy 1.9.0, pyright 1.1.350, and
pytype 2024.2.27.
'''.lstrip()

setup(name=name,
      version="1.0.0.20240311",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/mypy-extensions.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['mypy_extensions-stubs'],
      package_data={'mypy_extensions-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
