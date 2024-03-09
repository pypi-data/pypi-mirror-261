# -*- coding: utf-8 -*-
import sys

from setuptools import setup, find_packages

# Avoids IDE errors, but actual version is read from version.py
__version__ = ""
exec(open('mulanai/version.py').read())

if sys.version_info < (3,):
    sys.exit('Sorry, Python3 is required.')

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='mulanai',
    version=__version__,
    description='Text to vector Tool, encode text',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='XuMing',
    author_email='xuming624@qq.com',
    url='https://github.com/shibing624/mulanai',
    license="Apache License 2.0",
    zip_safe=False,
    python_requires=">=3.10.0",
    entry_points={"console_scripts": ["mulanai = mulanai.cli:main"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords='llm,agent',
    install_requires=[
        "jieba",
        "loguru",
        "transformers",
        "datasets",
        "tqdm",
        "scikit-learn",
        "pandas",
    ],
    packages=find_packages(exclude=['tests']),
    package_dir={'mulanai': 'mulanai'},
    package_data={'mulanai': ['*.*', 'data/*.txt']}
)
