# -*- coding: utf-8 -*-



try:
    import logging
    import multiprocessing
    import os
except:
    pass

import sys
py_version = sys.version_info[:2]

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
    documentation = open(os.path.join(here, 'doc.rst')).read()
except IOError:
    documentation = ''

testpkgs = []

install_requires = ['python-magic', 'Wand', 'PyPDF2', 'Pillow']

if py_version != (3, 2):
    # Babel not available on 3.2
    install_requires.append("Babel")

setup(
    name='PyPreviewGenerator',
    # this must be the same as the name above
    version='0.1.6',
    description='Generation of file previews',
    long_description=documentation,
    author='Algoo',
    author_email='clemalex20@gmail.com',
    url='https://github.com/herawo/file_previewer_poc',
    download_url='https://github.com/herawo/file_previewer_poc/archive/0.1.tar.gz',
    keywords=['preview', 'preview_generator', 'thumbnail'],
    classifiers=[],
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=testpkgs,
    package_data={'preview_generator': [
        'i18n/*/LC_MESSAGES/*.mo',
        'templates/*/*',
        'public/*/*'
    ]}
)