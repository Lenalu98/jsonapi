from setuptools import setup, find_packages

setup(
    name='jsonapi',
    version='0.1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    author='Yuchen Lu',
    author_email='lu.yuch@northeastern.edu',
    description='A Python package for custom JSON encoding and decoding.',
    install_requires=[],
)
