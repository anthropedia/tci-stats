from distutils.core import setup


setup(
    name='tcistats',
    version='1.0',
    author='Vincent Agnano',
    license='Copyright Anthropedia',
    long_description=open('readme.md').read(),
    install_requires=['pandas<=0.21'],
)
