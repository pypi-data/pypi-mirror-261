from setuptools import setup, find_packages

setup(
    name='hpscancli',
    version='1.0.0',
    author='Prasanna Reddy. Ch',
    author_email='prasannareddy_ch@outlook.com',
    description='A simple python CLI tool to connect to HP scanner devices over local network and scan documents with ease.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/prasannareddych/HPScanCLI',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'bs4',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'hpscancli = hpscancli.main:main'
        ]
    }
)
