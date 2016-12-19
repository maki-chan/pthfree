from setuptools import setup

setup(
    name='pthfree',
    version='1.1',
    url='https://github.com/maki-chan/pthfree',
    license='Public Domain',
    author='maki-chan',
    description='Grabs all current freeleeches from PTH',
    py_modules=[
        'pthglobals'
    ],
    scripts=[
        'pthfree'
    ],
    install_requires=[
        'requests'
    ]
)
