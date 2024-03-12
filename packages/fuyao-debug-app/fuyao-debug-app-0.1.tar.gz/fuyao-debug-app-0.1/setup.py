from setuptools import setup
from setuptools import find_packages

setup(
    name='fuyao-debug-app',
    version='0.1',
    py_modules=['src'],
    packages = find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        fuyao-debug-app=app:cli
    ''',
)
