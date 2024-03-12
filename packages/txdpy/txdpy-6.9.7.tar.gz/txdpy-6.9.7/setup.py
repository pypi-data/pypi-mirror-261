from distutils.core import setup
import setuptools
packages = ['txdpy']
setup(name='txdpy',
    version='6.9.7',
    author='唐旭东',
    packages=packages,
    package_dir={'requests': 'requests'},
    install_requires=[
        "lxml","loguru","tqdm","colorama","xlrd","pymysql","xlsxwriter","selenium","natsort"
    ])