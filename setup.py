from setuptools import setup, find_packages


def readme():
    with open('README.md') as file:
        return file.read()

setup(name='naughty_words',
      version='0.1',
      python_requires='>=3.6',
      long_description=readme(),
      description='A simple naughty word filter in python.',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: Apache License 2.0',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3.6',
          'Topic :: Text Processing :: Linguistic',
      ],
      keywords='naughty words profanities profanity filter bad words',
      url='https://github.com/52inc/python-naughty-words',
      author='Evan Owen',
      author_email='evan@52inc.com',
      license='Apache License 2.0',
      packages=find_packages(exclude=['tests']),
      package_data={'naughty_words': ['wordlists/*.txt']},
      install_requires=[],
      include_package_data=True,
      zip_safe=False
)