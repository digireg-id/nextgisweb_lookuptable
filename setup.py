import io
from setuptools import setup, find_packages

with io.open('VERSION', 'r') as fd:
    VERSION = fd.read().rstrip()

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
    version=VERSION,
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
