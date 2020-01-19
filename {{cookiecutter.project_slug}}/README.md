{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}
{% if is_open_source %}
<a href="https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}">
<img src="https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg" /></a>
</p>
{%- endif %}
{{ cookiecutter.project_short_description }}

## Features
-   TODO

# Credits
This package was created with Cookiecutter and the `cs01/cookiecutter-pypackage` project template.

[Cookiecutter](https://github.com/audreyr/cookiecutter)
[cs01/cookiecutter-pypackage](https://github.com/cs01/cookiecutter-pypackage)
