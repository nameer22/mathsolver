from setuptools import setup
import setuptools



# Dynamically retrieve the information
MATHSOLVER = __import__('mathsolver')
VERSION = MATHSOLVER.__version__
AUTHOR = MATHSOLVER.__author__
AUTHOR_EMAIL = MATHSOLVER.__email__
URL = MATHSOLVER.__url__

with open("README.md", "r") as f:
    long_description = f.read()

setup (
    name='mathsolver',
    version=VERSION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description='Decode natural language to solve mathemathical calculations',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Topic :: Text Processing :: General',
            'Topic :: Text Processing :: Linguistic',
            'Programming Language :: Python',
    ],
    include_package_data=True,
)
