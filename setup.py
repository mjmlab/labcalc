#!/usr/bin/env python3

import sys, platform, os

try:
    from setuptools import *
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
finally:
    from setuptools import *

from glob import glob

if sys.version_info < (3, 5):
    print >> sys.stderr, "ERROR: labcalc requires python 3.5 or greater"
    sys.exit()

__version__ = open(os.path.join('labcalc', 'VERSION')).read().strip()

SCRIPTS = glob('scripts/*')

def main():
    setup(  name = 'labcalc',
            version = __version__,
            description = 'Molecular Biology Calculator',
            url = 'https://github.com/mjmlab/labcalc',
            author = 'Mark J. Mandel',
            author_email = 'mandel01@gmail.com',
            license = 'BSD',
            packages = find_packages(),
            scripts = SCRIPTS,
            setup_requires = ['pytest-runner'],
            tests_require = ['pytest'],
            install_requires = ['pytest>=2.8.1',
                                'pytest-cov>=2.4.0',
                                'codecov>=2.0.5',
                                'click>=6.7'],
            classifiers = ['Development Status :: 4 - Beta',
                           'Intended Audience :: Science/Research',
                           'License :: OSI Approved :: BSD License',
                           'Operating System :: MacOS :: MacOS X',
                           'Operating System :: POSIX',
                           'Programming Language :: Python :: 3.5',
                           'Topic :: Scientific/Engineering :: Bio-Informatics',
                           ],

            zip_safe = False,
            include_package_data = True )


if __name__ == "__main__":
    main()
