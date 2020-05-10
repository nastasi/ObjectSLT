# This file is part of 'ObjectSLT' program.
#
#     Copyright (C) 2020-2020 Matteo Nastasi
#                          mailto: nastasi@alternativeoutput.it
#                                  matteo.nastasi@gmail.com
#                          web: http://www.alternativeoutput.it
#
#     'objectslt' is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     Nome-Programma is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with Nome-Programma.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
from objectslt import __version__

setup(name='objectslt',
      version=__version__,
      description='Minimal JSON template populator using ObjectPath as source of substitution.',
      url='https://github.com/nastasi/ObjectSLT',
      download_url = 'https://github.com/nastasi/ObjectSLT/archive/v' + __version__ + '.tar.gz',
      author='Matteo Nastasi',
      author_email='nastasi@alternativeoutput.it',
      license='GPLv3',
      packages=['objectslt'],
      install_requires=[
          'objectpath',
          'pytz', #  FIXME: missing in 'objectpath' deps,  added here
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Database',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3',
      ],
      entry_points = {
          'console_scripts': ['objectslt=objectslt.base:command'],
      },
      include_package_data=True,
      zip_safe=False
)
