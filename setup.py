from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='py_aws_create_pro',
    version='0.1.0',
    description='Python module for creating security group using boto3',
    long_description=readme,
    author='Quadyster_dev_team',
    author_email='mkola@quadyster.com',
    url='https://github.com/quad-cloud/py_aws_create_pro.git',
    packages=find_packages(exclude=('tests', 'docs'))
)