
from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Hello world app',
    ext_modules=cythonize("hellocy.pyx"),
    compiler_directives={'language_level': 3}, # not working
    language_level=3,
    zip_safe=False,

    # zip_safe = True
)

# now run this shell command
# python setup.py build_ext --inplace 