# My first package

This is a fantastic package for Python.

it say *both* hello and goodbye.

## into the package folder

```zsh
poetry build
export PYPI_USERNAME=__token__
export PYPI_PASSWORD=pypi-Ag....
poetry publish --build --username $PYPI_USERNAME --password $PYPI_PASSWORD
```
