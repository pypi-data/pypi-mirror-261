from setuptools import setup, find_packages
import codecs
import os



VERSION = '0.0.1'
DESCRIPTION = 'Creates patterns'


# Setting up
setup(
    name="patternal",
    version=VERSION,
    author="Arihant Pal",
    author_email="arihantpal2001@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'pattern', 'star_pattern', 'star'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
