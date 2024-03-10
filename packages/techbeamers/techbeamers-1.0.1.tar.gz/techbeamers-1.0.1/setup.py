# setup.py

from setuptools import setup, find_packages

setup(
    name='techbeamers',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'pycodestyle',
        'flake8',
        'mypy',
    ],
    entry_points={
        'console_scripts': [
            'techbeamers-analyzer=techbeamers.analyzer:main',
        ],
    },
    author='Meenakshi Agarwal',
    author_email='magarwal@example.com',
    description='Code Analyzer Tool by TechBeamers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://techbeamers.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

