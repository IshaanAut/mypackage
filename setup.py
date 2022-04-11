from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example pything package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/IshaanAut/mypackage',
    author='Ishaan Authar',
    author_email='ishaan.authar@absa.africa'
)