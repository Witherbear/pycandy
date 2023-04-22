from setuptools import setup

setup(
    name='pycandy',
    version='1.0.0',
    description='A retro Python game engine.',
    url='https://github.com/Witherbear/pycandy',
    author='Witherbear',
    author_email='witherbear@greenbear.ml',
    keywords='pygame retro game pycandy',
    packages=['pycandy'],
    install_requires=[
        'pygame>=2.0.0',
    ],
)
