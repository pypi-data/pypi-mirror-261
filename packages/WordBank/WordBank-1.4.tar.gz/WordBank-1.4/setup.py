from setuptools import setup, find_packages

setup(
    name="WordBank",
    version='1.4',
    packages=find_packages(),
    package_data={
    },
    install_requires=[
        'nltk',
    ],
)