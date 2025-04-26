from setuptools import setup, find_packages

setup(
    name="semantic_search_redis",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'redis',
        'sentence-transformers',
        'datasets',
        'numpy'
    ],
)
