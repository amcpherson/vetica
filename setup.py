from setuptools import setup, find_packages

setup(
    name='vetica',
    packages=find_packages(),
    package_data={'vetica': ['data/*.ttf']},
)
