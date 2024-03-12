from setuptools import setup, find_packages

setup(
    name='json-canvas',
    version='0.1.3',
    packages=find_packages(),
    install_requires=["dataclasses"],
    url='https://github.com/ethanzh/json-canvas-python',
    license='MIT',
    author='Ethan Zedler Houston',
    author_email='ethan.houston@gmail.com',
    description='A simple package to work with JSON Canvas',
)
