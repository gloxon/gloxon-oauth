from setuptools import setup 

setup(
    name = 'gloxon-oauth',
    version = '0.1.0',
    description = 'A module that provide a Python interface to the Gloxon Oauth API',
    url='https://github.com/gloxon/gloxon-oauth',
    author='Gloxon LLC',
    author_email='gloxongp@gmail.com',
    license = "MIT",
    packages = ['gloxonoauth'],
    install_requires = ['requests'],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3'
    ],
)