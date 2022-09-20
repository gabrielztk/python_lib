from setuptools import setup

setup(name='dev_aberto_gabrielztk',
      version='0.1',
      packages=['dev_aberto'],
      author="gabrielztk",
      license="MIT",
      install_requires=[
          "requests",
      ],
      scripts=['scripts/hello.py']
      )

