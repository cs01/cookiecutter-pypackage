# cs01 Cookiecutter PyPackage
<p align="center">

<a href="https://travis-ci.org/cs01/cookiecutter-pypackage"><img src="https://travis-ci.org/cs01/cookiecutter-pypackage.svg?branch=master" /></a>
</p>

-   GitHub repo: https://github.com/cs01/cookiecutter-pypackage/

## Features

-   [pytest](https://docs.pytest.org/en/latest/): The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.
-   [Travis-CI](https://travis-ci.org/): Ready for Travis Continuous Integration testing
-   [nox](https://pypi.org/project/nox/): Project automation and testing for multiple Python environments. Comes with a noxfile that runs tests, lint, builds and publishes the package to PyPI
-   [mypy](https://pypi.org/project/mypy/): Typing enabled, with PEP 561 support so your typing extends to consumers of your package
-   src dir: Directory structure uses `src` directory to ensure no accidental installations
-   [black](https://github.com/psf/black): Code is autoformatted with `black`


Made with [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/index.html), so you can modify the and fork this template easily.

## Quickstart


Generate the project with [pipx](https://github.com/pipxproject/pipx/):

```
pipx run https://github.com/cs01/cookiecutter-pypackage/
```

### Not Exactly What You Want?

See [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) for the original template, as well as other popular templates.
