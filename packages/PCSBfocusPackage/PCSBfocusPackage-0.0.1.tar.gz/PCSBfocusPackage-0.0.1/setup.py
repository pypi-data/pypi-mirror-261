from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A python package for PCSB Focus student web application'
LONG_DESCRIPTION = 'A python package made to get data from the PCSB Focus student web application'

# Setting up
setup(
    name="PCSBfocusPackage",
    version=VERSION,
    author="Aidan Bruner",
    author_email="Aidanbruner789@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['selenium'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)



