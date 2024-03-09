from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='areacalc',
  version='0.0.1',
  author='k1zon',
  description='This is the simple area calculator of different 2d figures.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  packages=find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3.11',
  ],
  keywords='areacalc ',
  project_urls={
    'GitHub': 'https://github.com/K1Zon/AreaCalc_Lib'
  },
  python_requires='>=3.6'
)