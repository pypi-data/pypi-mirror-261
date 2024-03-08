#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name="dataskillhub",
    version="1.0.19",
    description="Anonymisation et filtrage des termes dans le CV, décoration et style des CV produits.",  # noqa:
    author="Xin Yao",
    author_email="xin.yao@datalyo.com",
    url="https://gitlab-datalyo.francecentral.cloudapp.azure.com/dossier-de-comp-tences/dossiercompetence",  # noqa:
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click","pydantic","PyYAML","Markdown","weasyprint","Jinja2","flake8","black","pytest"],  # noqa:
    entry_points={
        "console_scripts": [
            "dsh_init = data_skill_hub.main:init",
            "dsh_consultant_export = data_skill_hub.main:export"
        ]
    },
)
