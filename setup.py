from setuptools import setup, find_packages

VERSION = '0.1.7'
DESCRIPTION = 'private modul'

# Setting up
setup(
    name="xnoxs",
    version=VERSION,
    author="xnoxs-dev",
    author_email="<khaerudin2119@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['xnoxs'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
