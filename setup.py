from setuptools import setup, find_packages
import sys, os

version = '0.0'

requires = (
    'nextgisweb',
)

entry_points = {
    'nextgisweb.packages': [
        'nextgisweb_lookuptable = nextgisweb_lookuptable:pkginfo',
    ],

    'nextgisweb.amd_packages': [
        'nextgisweb_lookuptable = nextgisweb_lookuptable:amd_packages',
    ],

}

setup(
    name='nextgisweb_lookuptable',
    version=version,
    description="",
    long_description="",
    classifiers=[],
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points=entry_points,
)
