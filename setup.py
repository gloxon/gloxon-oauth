from setuptools import setup 

setup(
    name = 'gloxon',
    version = '0.1.0',
    description = 'Python bindings to Gloxon LLC services. This package contains no code at the moment.',
    url='https://gloxoninc.com',
    author='Gloxon LLC',
    author_email='gloxongp@gmail.com',
    license = "MIT",
    packages = ['gloxon'],
    install_requires = ['requests'],

    classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3'
    ],
)