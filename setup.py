import pathlib
from setuptools import setup, find_packages

VERSION = 'alpha'
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(name='gym_game',
      version=VERSION,
      description='Fill the slots game',
      long_description=README,
      long_description_content_type="text/markdown",
      author='Shaked Zychlinski',
      license='Apache License 2.0',
      author_email='shakedzy@gmail.com',
      url='https://github.com/shakedzy/dython',
      install_requires=['numpy'],
      packages=find_packages(),
)