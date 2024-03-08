from setuptools import setup, find_packages

setup(
    name='ferramentas_basicas_pln',
    version='0.1',
    packages=find_packages(),
    install_requires=['regex',
                      'unidecode',                   
    ]
)