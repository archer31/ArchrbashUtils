import setuptools

with open('README.md', 'r') as readme:
  long_description=readme.read()

setuptools.setup(
  name='ArchrBashUtils',
  description='A set of bash utilities that I made for convenience',
  long_description=long_description,
  version='0.4.0',
  author='Alexander Corley',
  author_email='xandy@corley.org',
  packages=setuptools.find_packages(),
  entry_points={
    'console_scripts':[
      'configfiles = configfiles.configfiles:main',
      'ctouch = ctouch.ctouch:main',
      'linecheck = linecheck.linecheck:main',
      'sline = sline.sline:main',
    ]
  },
  package_data={
    'configfiles': ['configfiles.json'],
  }
)
