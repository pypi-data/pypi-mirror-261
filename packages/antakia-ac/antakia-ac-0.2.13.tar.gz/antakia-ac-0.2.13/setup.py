from setuptools import setup
from Cython.Build import cythonize


setup(
    name='antakia-ac',
    version='0.2.13',
    install_requires=[
        'numba',
        'scipy',
        'scikit-learn',
        'tomaster',
        'antakia-core',
        'importlib-metadata; python_version>="3.11"',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    ext_modules=cythonize("src/*pyx", compiler_directives={'language_level': 3}),
)