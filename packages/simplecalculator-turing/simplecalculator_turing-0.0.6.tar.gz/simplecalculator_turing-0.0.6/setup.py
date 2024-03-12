from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='simplecalculator_turing',
    version='0.0.6',
    description='A simple command-line calculator program that can perform basic arithmetic operations and nth root calculation.',
    packages=find_packages(exclude=('app.simplecalculator.test',)),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/TuringCollegeSubmissions/arocas-DWWP.1.5',
    author='Armin Rocas',
    author_email='armin.rocas@live.com',
    license='GPL-3.0',
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    entry_points={'console_scripts': ['simplecalculator = app.simplecalculator.src.calculator:main']}
)
