## Long description

## Using setup.py

```shell
pip install twine
```

```shell
python3 setup.py sdist bdist_wheel
```

```shell
twine upload dist/*
```

## Using pyproject.toml

```shell
pip install -e .
pip list
```

```shell
python3 -m build
```

```shell
pip install twine
twine upload dist/*
```


### setup.py

```shell

# from setuptools import setup, find_packages
#
# setup(
#   name = "zigzag-cases",
#   version = "0.3.0",
#   author = "Avinash R",
#   description = "This is short description",
#   long_description = open("README.md").read(),
#   long_description_content_type="text/markdown"
# )
```
