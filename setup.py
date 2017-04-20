from setuptools import setup, find_packages
from mozlotov import __version__


install_requires = ['PyFxA', 'requests', 'requests_hawk']
description = ''

for file_ in ('README', 'CHANGELOG'):
    with open('%s.rst' % file_) as f:
        description += f.read() + '\n\n'


classifiers = ["Programming Language :: Python",
               "License :: OSI Approved :: Apache Software License",
               "Development Status :: 1 - Planning"]


setup(name='mozlotov',
      version=__version__,
      url='https://github.com/loads/molotov',
      packages=find_packages(),
      long_description=description.strip(),
      description=("Mozilla Helpers for Molotov"),
      author="Tarek Ziade",
      author_email="tarek@ziade.org",
      include_package_data=True,
      zip_safe=False,
      classifiers=classifiers,
      install_requires=install_requires)
