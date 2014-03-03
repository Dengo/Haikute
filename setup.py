from setuptools import setup

long_description = """
A package containing the Haikute haiku generator app.
"""

setup(
    name="haikute",
    version="0.1-dev",
    description="Basic Haiku Generator",
    long_description=long_description,
    url='http://github.com/markcharyk/haikute',
    author='Tsnaomi, markcharyk, and lordsheepy',
    author_email='<your.email@domain.com',
    license='MIT',
    packages=[],
    install_requires=['PyYAML >= 3.10',
                      'argparse >= 1.2.1',
                      'gunicorn >= 18.0',
                      'nltk==2.0.4'
                      ]
)
