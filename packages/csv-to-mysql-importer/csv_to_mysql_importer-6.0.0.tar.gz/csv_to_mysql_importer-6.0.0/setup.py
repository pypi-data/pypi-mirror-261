from setuptools import setup, find_packages

setup(
    name='csv_to_mysql_importer',
    version='6.0.0',
    description='A package for importing CSV files into a MySQL database',
    author='Md Arfaan Baig',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'mysql-connector-python',
    ],
    entry_points={
        'console_scripts': [
            'csv_import=csv_to_mysql_importer.main:main',
        ],
    },
)
