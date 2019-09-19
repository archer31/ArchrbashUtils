import setuptools

with open('README.md', 'r') as readme:
  long_description=readme.read()

setuptools.setup(
  name='ArchrBashUtils',
  description='A set of bash utilities that I made for convenience',
  long_description=long_description,
  version='0.0.0',
  packages=setuptools.find_packages()
)
