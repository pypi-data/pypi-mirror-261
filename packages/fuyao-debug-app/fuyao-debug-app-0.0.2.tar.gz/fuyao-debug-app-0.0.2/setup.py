from setuptools import setup

setup(
    name='fuyao-debug-app',
    version='0.0.2',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    py_modules=['app', 'db', 'utils'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        fuyao-debug-app=app:cli
    ''',
)
