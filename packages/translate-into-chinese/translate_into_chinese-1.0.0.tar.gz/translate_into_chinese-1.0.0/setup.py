from distutils.core import setup
import setuptools
packages = ['translate_into_chinese']
setup(name='translate_into_chinese',
    version='1.0.0',
    author='唐旭东',
    packages=packages,
    package_dir={'requests': 'requests'},
    install_requires=[
        "requests"
    ])