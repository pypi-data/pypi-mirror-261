from setuptools import setup, find_packages


def requires():
    with open('requirements.txt') as file:
        return file.read().split('\n')


setup(
    name='flet_abp_cli',
    version='1.0.7',
    author='ShadowP1e',
    author_email='andrey.bakov.2006@gmail.com',
    description='This is my first module',
    packages=find_packages(),
    install_requires=['click'],
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'flet-abp-cli = flet_abp_cli.main:cli'
        ]
    }
)
