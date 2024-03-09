from setuptools import setup, find_packages

setup(
    name='my_model_package',
    version='1.0.2',
    packages=find_packages(),
    include_package_data=True,
#    package_data={'my_model_package': ['*.h5']},  # Include all .h5 files in my_model_package directory
    install_requires=[
        'tensorflow>=2.0',
        'transformers',
    ],
)
