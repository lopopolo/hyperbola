"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# To use a consistent encoding
from codecs import open
from pathlib import Path

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

here = Path(__file__).resolve().parent

# Get the long description from the README file
with open(str(here.joinpath('README.md')), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hyperbola',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.102.0',

    description='hyperbola: a django website',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/lopopolo/hyperbola',

    # Author details
    author='Ryan Lopopolo',
    author_email='rjl@hyperbo.la',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: JavaScript',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',

        'Framework :: Django',
        'Framework :: Django :: 1.11',

    ],

    # What does your project relate to?
    keywords='django web website webpack',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'Django ~= 1.11.0',
        'django-localflavor',
        'django-missing',
        'django-mysql',
        'django-redis',
        'django-redis-cluster',
        'django-s3-storage',
        'django-stdimage',
        'gunicorn',
        'markdown',
        'mysqlclient >= 1.3.3',
        'Pillow',
        'pytz',
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': [
            'bumpversion',
            'django-debug-toolbar',
            'django-debug-toolbar-template-timings >= 0.7',
            'flake8',
            'isort',
            'pep257',
            'pep8',
            'pip-tools',
            'pylint',
            'pylint-django',
            'yapf',
        ],
        'tools': [
            'ansible-lint',
        ],
    },
)
