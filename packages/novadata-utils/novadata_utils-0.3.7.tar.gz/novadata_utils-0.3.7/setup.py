from setuptools import find_packages, setup

with open("README.rst", "r", encoding="utf-8") as fh:
    readme = fh.read()

setup(
    name="novadata_utils",
    version="0.3.7",
    url="https://github.com/TimeNovaData/novadata_utils/",
    license="MIT License",
    author="Flávio Silva",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author_email="flavio.nogueira.profissional@gmail.com",
    keywords="Django, utils, ndt, novadata, nova data, nova, data",
    description="novadata utils",
    packages=find_packages(),
    install_requires=[
        "django",
        "djangorestframework",
        "django-admin-list-filter-dropdown",
        "django-admin-rangefilter",
        "django-advanced-filters",
        "django-crum",
        "django-import-export",
        "django-object-actions",
    ],
    project_urls={
        "GitHub": "https://github.com/TimeNovaData/novadata_utils/",
    },
)
