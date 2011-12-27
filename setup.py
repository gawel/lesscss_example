import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = ['pyramid', 'pyramid_debugtoolbar',
            'pyramid_fanstatic']

setup(name='lesscss_example',
      version='0.0',
      description='lesscss_example',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="lesscss_example",
      entry_points="""\
      [paste.app_factory]
      main = lesscss_example:main

      # Fanstatic resource library
      [fanstatic.libraries]
      lesscss_example = lesscss_example.resources:library

      # A console script to serve the application and monitor also static
      # resources
      [console_scripts]
      pserve-fanstatic = lesscss_example.resources:pserve
      """,
      )
