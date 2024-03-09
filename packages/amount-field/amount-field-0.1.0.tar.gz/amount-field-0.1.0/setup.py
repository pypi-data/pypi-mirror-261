from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='amount-field',  # Replace with your package name
    version='0.1.0',  # Update with your package version
    author='Syed Maaz Hassan',
    author_email='hafizmaazhassan33@gmail.com',
    description='A Django app for handling amounts, currencies, and prices',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/SyedMaazHassan/amount_field',  # Update with your GitHub repository URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'Django'
    ],
)
