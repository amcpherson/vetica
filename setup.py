from setuptools import setup, find_packages

setup(
    name='vetica',
    packages=find_packages(),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    package_data={'vetica': ['data/*.ttf']},
)
