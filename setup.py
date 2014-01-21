import os
from distutils.core import setup, Extension


here = os.path.abspath(os.path.dirname(__file__))
src = os.path.join(here, "src")


module1 = Extension(
    'decquad',
    sources=[os.path.join(src, 'decquadmodule.c')],
    include_dirs=[])

setup(name='decquad',
      url='https://github.com/cazino/decquad',
      author='emmanuel cazenave',
      author_email='emmanuel.cazenave@gmail.com',
      version='0.1',
      description='',
      ext_modules=[module1])
