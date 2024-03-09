from setuptools import setup, find_packages

with open('../README.md', 'r') as f:
    long_description = f.read()

setup(
    name='indianlang-nlp',
    version='0.0.1.5',
    packages=find_packages(),
    install_requires=[
        'keras',
        'tensorflow',
        'gdown',
    ],
    author='Amey Pandit',
    url="https://github.com/panditamey/indianlang-nlp",   
    long_description=long_description,
    long_description_content_type='text/markdown',
)
