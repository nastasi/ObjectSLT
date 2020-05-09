from setuptools import setup

setup(name='objectslt',
      version='0.1',
      description='Minimal JSON template populator using ObjectPath as source of substitution.',
      url='https://github.com/nastasi/objectslt',
      author='Matteo Nastasi',
      author_email='nastasi@alternativeoutput.it',
      license='GPLv3',
      packages=['objectslt'],
      install_requires=[
          'objectpath',
      ],
      entry_points = {
          'console_scripts': ['objectslt=objectslt.base:command'],
      },
      zip_safe=False)
