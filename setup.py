from setuptools import setup
from objectslt import __version__

setup(name='objectslt',
      version=__version__,
      description='Minimal JSON template populator using ObjectPath as source of substitution.',
      url='https://github.com/nastasi/objectslt',
      author='Matteo Nastasi',
      author_email='nastasi@alternativeoutput.it',
      license='GPLv3',
      packages=['objectslt'],
      install_requires=[
          'objectpath',
          'pytz', #  FIXME: missing objectpath added
      ],
      entry_points = {
          'console_scripts': ['objectslt=objectslt.base:command'],
      },
      zip_safe=False)
