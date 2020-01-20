{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}
<p align="center">
{% if is_open_source %}
<a href="https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}">
<img src="https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg" /></a>
{%- endif %}
<a href="https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}"><img src="https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?branch=master" /></a>
</p>
{{ cookiecutter.project_short_description }}

## Features
-   TODO

# Credits
This package was created with Cookiecutter and the `cs01/cookiecutter-pypackage` project template.

[Cookiecutter](https://github.com/audreyr/cookiecutter)

[cs01/cookiecutter-pypackage](https://github.com/cs01/cookiecutter-pypackage)
