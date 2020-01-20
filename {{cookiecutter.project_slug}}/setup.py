#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore

with open("README.md") as readme_file:
    readme = readme_file.read()


{%- set license_classifiers = {
    "MIT license": "License :: OSI Approved :: MIT License",
    "BSD license": "License :: OSI Approved :: BSD License",
    "ISC license": "License :: OSI Approved :: ISC License (ISCL)",
    "Apache Software License 2.0": "License :: OSI Approved :: Apache Software License",
    "GNU General Public License v3": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
} %}

setup(
    author="{{ cookiecutter.full_name.replace("\"", "\\\"") }}",
    author_email="{{ cookiecutter.email }}",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
{%- if cookiecutter.open_source_license in license_classifiers %}
        "{{ license_classifiers[cookiecutter.open_source_license] }}",
{%- endif %}
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="{{ cookiecutter.project_short_description }}",
    {%- if "no" not in cookiecutter.command_line_interface|lower %}
    entry_points={"console_scripts": ["{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main",],},
    {%- endif %}
    install_requires=[],
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"{{ cookiecutter.project_slug }}": ["py.typed"]},
    include_package_data=True,
    keywords="{{ cookiecutter.project_slug }}",
    name="{{ cookiecutter.project_slug }}",
    package_dir={"": "src"},
    packages=find_packages(include=["src/{{ cookiecutter.project_slug }}", "src/{{ cookiecutter.project_slug }}.*"]),
    setup_requires=[],
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.version }}",
    zip_safe=False,
)
