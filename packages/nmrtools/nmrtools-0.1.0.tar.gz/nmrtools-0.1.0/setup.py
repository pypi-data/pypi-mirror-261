from setuptools import find_packages, setup

with open('app/README.md', 'r') as file:
    long_description = file.read()

setup(
    name='nmrtools',
    version='0.1.0',
    description='A package for NMR data processing',
    package_dir={'': 'app'},
    packages=find_packages(where='nmrtools'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pratiman-de/Bruker-to-Numpy',
    author='pratiman-de',
    license='MIT',
    py_modules=['nmrtools'],
    install_requires=[
        'Click',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'nmrtools = nmrtools:nmr',
            'np2ser = nmrtools:np2ser',
            'ser2np = nmrtools:ser2np',
        ],
    },
)

