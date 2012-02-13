import os
from setuptools import setup


readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


setup(
    name='Padak',
    version='0.1',
    description='EDSL template engine written in Python',
    url='https://github.com/kimjayd/padak',
    long_description=readme,
    author='Hyunjun Kim',
    author_email='kim@hyunjun.kr',
    license='MIT License',
    packages=['padak'],
    extras_require={'docs': ['Sphinx']}
)
