from setuptools import setup, find_packages

setup(
    name='my_model_package',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        #dependencies the package requires
        'tensorflow>=2.0',
        'transformers',
    ],
)
