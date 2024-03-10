from setuptools import setup


setup(
    name             = 'Wilt',
    version          = '0.0.1',
    author           = 'saaj',
    author_email     = 'mail@saaj.me',
    packages         = ['wilt'],
    license          = 'LGPL-3.0-only',
    description      = 'A collection of codebase visualisations for architects',
    long_description = open('README.rst', 'rb').read().decode('utf-8'),
    keywords         = 'code-metrics code-quality',
    url              = 'https://heptapod.host/saajns/wilt',
    classifiers      = [
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Intended Audience :: Developers',
    ],
    entry_points     = {'console_scripts': ['wilt = wilt.cli:main']},
    install_requires = [],
)
