#! /usr/bin/env python

DESCRIPTION = "catsHTM: fast access to large astronomical catalogs"
#LONG_DESCRIPTION = """ """

DISTNAME = 'pysedm'
AUTHOR = 'Maayane T. Soumagnac'
MAINTAINER = 'Maayane T. Soumagnac' 
MAINTAINER_EMAIL = 'maayane.soumagnact@weizmann.ac.il'
URL = 'https://github.com/maayane/catsHTM'
#LICENSE = 'BSD (3-clause)'
#DOWNLOAD_URL = 'https://github.com/MickaelRigault/pysedm/tarball/0.9'
#VERSION = '0.9.3'

try:
    from setuptools import setup, find_packages
    _has_setuptools = False
except ImportError:
    from distutils.core import setup

def check_dependencies():
    install_requires = []

    # Just make sure dependencies exist, I haven't rigorously
    # tested what the minimal versions that will work are
    # (help on that would be awesome)
    try:
        import propobject
    except ImportError:
        install_requires.append('propobject')
        
    return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()

    if _has_setuptools:
        packages = find_packages()
        print(packages)
    else:
        # This should be updated if new submodules are added
        packages = ['catsHTM',
                    "catsHTM.script",
                    "catsHTM.utils"]

    setup(name=DISTNAME,
          author=AUTHOR,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          scripts=["bin/ccd_to_cube.py" ,
                   "bin/display_cube.py",
                   "bin/extract_star.py",
                   "bin/cube_quality.py",
                   "bin/derive_wavesolution.py",
                   "bin/quality_check.py"],
          packages=packages,
          include_package_data=True,
          package_data={'pysedm': ['data/*.*']},
          classifiers=[
              'Intended Audience :: Science/Research',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3.5',              
              'License :: OSI Approved :: BSD License',
              'Topic :: Scientific/Engineering :: Astronomy',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'],
      )