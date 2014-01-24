import os
from distutils.core import setup, Extension


here = os.path.abspath(os.path.dirname(__file__))
src = os.path.join(here, "src")
libmpdec_src = os.path.join(here, 'libmpdec')


def _decimal_ext():
    # Ripped from http://hg.python.org/cpython/file/c4a2d0538441/setup.py
    extra_compile_args = []
    undef_macros = []

    include_dirs = [libmpdec_src]
    libraries = []
    sources = [
        'src/decquadmodule.c',
        'libmpdec/basearith.c',
        'libmpdec/constants.c',
        'libmpdec/context.c',
        'libmpdec/convolute.c',
        'libmpdec/crt.c',
        'libmpdec/difradix2.c',
        'libmpdec/fnt.c',
        'libmpdec/fourstep.c',
        'libmpdec/io.c',
        'libmpdec/memory.c',
        'libmpdec/mpdecimal.c',
        'libmpdec/numbertheory.c',
        'libmpdec/sixstep.c',
        'libmpdec/transpose.c',
    ]
    depends = [
        'docstrings.h',
        'libmpdec/basearith.h',
        'libmpdec/bits.h',
        'libmpdec/constants.h',
        'libmpdec/convolute.h',
        'libmpdec/crt.h',
        'libmpdec/difradix2.h',
        'libmpdec/fnt.h',
        'libmpdec/fourstep.h',
        'libmpdec/io.h',
        'libmpdec/memory.h',
        'libmpdec/mpdecimal.h',
        'libmpdec/numbertheory.h',
        'libmpdec/sixstep.h',
        'libmpdec/transpose.h',
        'libmpdec/typearith.h',
        'libmpdec/umodarith.h',
    ]

    config = {
        'x64': [('CONFIG_64', '1'), ('ASM', '1')],
    }

    cc = 'gcc -pthread'
    define_macros = config['x64']

    # Increase warning level for gcc:
    if 'gcc' in cc:
        cmd = ("echo '' | %s -Wextra -Wno-missing-field-initializers -E - "
               "> /dev/null 2>&1" % cc)
        ret = os.system(cmd)
        if ret >> 8 == 0:
            extra_compile_args.extend(['-Wextra',
                                       '-Wno-missing-field-initializers'])

    # Uncomment for extra functionality:
    #define_macros.append(('EXTRA_FUNCTIONALITY', 1))
    ext = Extension(
        'decquad',
        include_dirs=include_dirs,
        libraries=libraries,
        define_macros=define_macros,
        undef_macros=undef_macros,
        extra_compile_args=extra_compile_args,
        sources=sources,
        depends=depends
    )
    return ext


module1 = Extension(
    'decquad',
    include_dirs=[libmpdec_src],
    sources=[os.path.join(src, 'decquadmodule.c')])

setup(name='decquad',
      url='https://github.com/cazino/decquad',
      author='emmanuel cazenave',
      author_email='emmanuel.cazenave@gmail.com',
      version='0.1',
      description='',
      ext_modules=[_decimal_ext()])
